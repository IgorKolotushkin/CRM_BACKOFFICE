import pytest
from django.test import Client
from django.urls import reverse

from .models import Product, Lead

csrf_client = Client(enforce_csrf_checks=True)


def test_login_user():
    data = {
        'name': 'igor',
        'password': '123',
    }
    url = reverse('crm_auth:login')
    response = csrf_client.post(url, data)


def test_create_product(db):
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
    # assert response.context_data['product'].name == 'product'
    assert response.context_data['product'].cost == 1000


def test_superuser_get_delete_product(admin_client):
    count_products = len(Product.objects.all())
    product = Product.objects.create(name='product_1', cost=100)
    url = reverse('office:delete-product', kwargs={'pk': product.pk})
    response = admin_client.delete(url)
    assert response.status_code == 302
    assert len(Product.objects.all()) == count_products


@pytest.mark.django_db(transaction=True)
def test_superuser_get_edit_product(admin_client):
    product = Product.objects.create(name='product_1', cost=100)
    url = reverse('office:edit-product', kwargs={'pk': product.pk})
    data = {
        'name': 'product_2',
        'cost': 200,
    }
    response = admin_client.put(url, data)
    assert response.status_code == 200
    edit_product = Product.objects.get(pk=product.pk)
    assert edit_product.name == 'product_2'


def test_superuser_create_product(admin_client):
    data = {
        'name': 'product_test',
        'cost': 500,
    }
    url = reverse('office:create-product')
    response = admin_client.post(url, data)
    assert response.status_code == 200


# @pytest.mark.django_db
def test_view_login_inactive_user(client):
    url = reverse('office:index')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/stat/'


# @pytest.mark.django_db
def test_superuser_view_leads_list(admin_client):
    lead = Lead.objects.first()
    url = reverse('office:leads')
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "leads/leads-list.html" in response.template_name
    assert response.context_data['leads'][0].first_name == lead.first_name
    assert response.context_data['leads'][0].email == lead.email


def test_superuser_add_lead_db(admin_client):
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


def test_superuser_create_lead(admin_client):
    # csrf_client.login(username="igor", password="123")
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


