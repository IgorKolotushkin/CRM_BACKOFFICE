"""Модуль с тестами для CRM"""
import datetime

from django.test import Client
from django.urls import reverse

from .models import Product, Lead, Customer, Ads, Contract

csrf_client = Client(enforce_csrf_checks=True)


def test_login_user():
    data = {
        'name': 'igor',
        'password': '123',
    }
    url = reverse('crm_auth:login')
    response = csrf_client.post(url, data)


def test_create_product() -> None:
    """
    тест создания продукта в базе данных
    :param db:
    :return: None
    """
    count_product = len(Product.objects.all())
    product = Product.objects.create(name="product", cost=1000)
    assert product.name == "product" and product.cost == 1000

    count_product_new = len(Product.objects.all())
    assert count_product + 1 == count_product_new


def test_superuser_get_products(admin_client):
    product = Product.objects.first()
    url = reverse('office:products')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.context_data['products'][0].name == product.name
    assert response.context_data['products'][0].cost == product.cost


def test_superuser_get_detail_product(admin_client):
    url = reverse('office:detail-product', kwargs={'pk': 1})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.context_data['product'].cost == 10000


def test_superuser_get_delete_product(admin_client):
    count_products = len(Product.objects.all())
    product = Product.objects.create(name='product_1', cost=100)
    url = reverse('office:delete-product', kwargs={'pk': product.pk})
    response = admin_client.delete(url)
    assert response.status_code == 302
    assert len(Product.objects.all()) == count_products


# @pytest.mark.django_db
def test_superuser_get_edit_product(admin_client):
    product = Product.objects.create(name='product_1', cost=100)
    url = reverse('office:edit-product', kwargs={'pk': product.pk})
    data = {
        'name': 'product_2',
        'cost': 200,
    }
    response = admin_client.put(url, data)
    assert response.status_code == 200


def test_superuser_create_product(admin_client):
    data = {
        'name': 'product_test',
        'cost': 500,
    }
    url = reverse('office:create-product')
    response = admin_client.post(url, data)
    assert response.status_code == 200


def test_view_login_inactive_user(client):
    url = reverse('office:index')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/stat/'


def test_superuser_view_leads_list(admin_client):
    lead = Lead.objects.first()
    url = reverse('office:leads')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "leads/leads-list.html" in response.template_name
    assert response.context_data['leads'][0].first_name == lead.first_name
    assert response.context_data['leads'][0].email == lead.email


def test_superuser_view_detail_lead(admin_client):
    lead = Lead.objects.first()
    url = reverse('office:detail-lead', kwargs={'pk': lead.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.context_data['lead'].first_name == lead.first_name


def test_add_lead_db() -> None:
    """
    Тест для проверки создания лида в базе данных.
    :return: None
    """
    count_leads = len(Lead.objects.all())
    lead = Lead.objects.create(
        first_name='first_test',
        last_name='last_test',
        email='email@email.com',
        phone='89001111111'
    )
    assert lead.first_name == 'first_test'
    assert lead.email == 'email@email.com'
    assert len(Lead.objects.all()) == count_leads + 1


def test_superuser_create_lead(admin_client) -> None:
    """
    Тест для проверки View создания лида.
    :param admin_client:
    :return: None
    """
    data = {
        'first_name': 'first_test_2',
        'last_name': 'last_test_2',
        'email': 'email@email_1.com',
        'phone': '89001111111',
        'ads': 'ads',
    }
    url = reverse('office:create-lead')
    response = admin_client.post(url, data)
    assert response.status_code == 200


def test_superuser_edit_lead(admin_client) -> None:
    """
    Тест для проверки View редактирования лида.
    :param admin_client:
    :return: None
    """
    lead = Lead.objects.first()
    data = {
        'first_name': 'first_test_3',
        'last_name': 'last_test_3',
        'email': 'email@email_3.com',
        'phone': '89001111111',
        'ads': 'ads',
    }
    url = reverse('office:edit-lead', kwargs={'pk': lead.pk})
    response = admin_client.put(url, data)
    assert response.status_code == 200


def test_superuser_delete_lead(admin_client) -> None:
    """
    Тест для проверки View для удаления лида.
    :param admin_client:
    :return: None
    """
    count_lead = len(Lead.objects.all())
    lead = Lead.objects.first()
    url = reverse('office:delete-lead', kwargs={'pk': lead.pk})
    response = admin_client.delete(url)
    assert response.status_code == 302
    assert len(Lead.objects.all()) == count_lead - 1


def test_superuser_view_customers_list(admin_client) -> None:
    """
    Тест для проверки View просмотра всех customer.
    :param admin_client:
    :return: None
    """
    url = reverse('office:customers')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "customers/customers-list.html" in response.template_name
    assert response.context_data['customers'][0].lead
    assert response.context_data['customers'][0].contract


def test_superuser_view_detail_customer(admin_client) -> None:
    """
    Тест для проверки View просмотра детальной информации о customer.
    :param admin_client:
    :return: None
    """
    customer = Customer.objects.first()
    url = reverse('office:detail-customer', kwargs={'pk': customer.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.context_data['customer'].lead == customer.lead


def test_add_customer_in_db() -> None:
    """
    Тест для проверки создания customer в базе данных.
    :return: None
    """
    count_customers = len(Customer.objects.all())
    customer = Customer.objects.create(
        lead_id=1,
    )
    assert customer.lead.first_name == 'Igor1'
    assert len(Customer.objects.all()) == count_customers + 1


def test_superuser_delete_customer(admin_client) -> None:
    """
    Тест для проверки view по удалению customer
    :param admin_client:
    :return: None
    """
    customer = Customer.objects.first()
    url = reverse('office:delete-customer', kwargs={'pk': customer.pk})
    response = admin_client.delete(url)
    assert response.status_code == 302


def test_superuser_view_ads_list(admin_client) -> None:
    """
    Тест для проверки View для просмотра всех рекламных компаний
    :param admin_client:
    :return: None
    """
    url = reverse('office:ads')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "ads/ads-list.html" in response.template_name
    assert response.context_data['ads'][0].name


def test_superuser_view_detail_ad(admin_client) -> None:
    """
    Тест пля проверки View для просмотра детальной информации о рекламной компании.
    :param admin_client:
    :return: None
    """
    ad = Ads.objects.first()
    url = reverse('office:detail-ad', kwargs={'pk': ad.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.context_data['ads'].name == ad.name


def test_superuser_delete_ad(admin_client) -> None:
    """
    Тест для проверки view по удалению ad
    :param admin_client:
    :return: None
    """
    ad = Ads.objects.first()
    url = reverse('office:delete-ad', kwargs={'pk': ad.pk})
    response = admin_client.delete(url)  # исправить в базе каскадное удаление
    assert response.status_code == 302


def test_add_ad_in_db() -> None:
    """
    Тест для проверки создания рекламной компании в базе данных.
    :return: None
    """
    count_ads = len(Ads.objects.all())
    ad = Ads.objects.create(
        name='ad',
        product=1,
        channel='channel',
        budget=1,
    )
    assert ad.name == 'ad'
    assert len(Ads.objects.all()) == count_ads + 1


def test_superuser_view_contracts_list(admin_client) -> None:
    """
    Тест для проверки View для просмотра всех контрактов
    :param admin_client:
    :return: None
    """
    url = reverse('office:contracts')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "contracts/contracts-list.html" in response.template_name
    assert response.context_data['contracts'][0].name


def test_superuser_view_detail_contract(admin_client) -> None:
    """
    Тест для проверки View просмотра детальной информации о контракте.
    :param admin_client:
    :return: None
    """
    contract = Contract.objects.first()
    url = reverse('office:detail-contract', kwargs={'pk': contract.pk})
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.context_data['contract'].name == contract.name


def test_superuser_delete_contract(admin_client) -> None:
    """
    Тест для проверки view по удалению контракта
    :param admin_client:
    :return: None
    """
    contract = Contract.objects.first()
    url = reverse('office:delete-contract', kwargs={'pk': contract.pk})
    response = admin_client.delete(url)
    assert response.status_code == 302


def test_add_contract_in_db() -> None:
    """
    Тест для проверки добавления контракта в базе данных.
    :return: None
    """
    product = Product.objects.first()
    count_contracts = len(Contract.objects.all())
    contract = Contract.objects.create(
        name='contract',
        start_date=datetime.datetime.now().date().strftime(format='%d.%m.%Y'),
        end_date=datetime.datetime.now().date().strftime(format='%d.%m.%Y'),
        product=product.pk,
        cost=100.0,
        file='file'
    )
    assert contract.name == 'contract'
    assert len(Contract.objects.all()) == count_contracts + 1
