import json

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User, Group, Permission
from django.views.decorators.csrf import csrf_exempt
import pytest

from .models import Product, Lead, Ads, Contract, Customer

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
    csrf_client.login(username="igor", password="123")

    data = {
        'first_name': 'first_test_2',
        'last_name': 'last_test_2',
        'email': 'email@email_1.com',
        'phone': '89001111111',
        'ads': 'ads',
    }
    count_lead = len(Lead.objects.all())
    url = reverse('office:create-lead')
    # response = admin_client.post(url, data)
    response = csrf_client.post(url, data)
    assert response.status_code == 200
    # assert response.context['form'] == ''
    assert count_lead + 1 == len(Lead.objects.all())

