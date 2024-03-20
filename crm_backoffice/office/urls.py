"""Модуль с url адресами для crm"""
from django.urls import path

from .views import (
    OfficeStatView,
    CustomerView,
    CustomerCreateView,
    LeadView,
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadUpdateView,
    LeadToCustomerView,
    CustomerDetailView,
    CustomerDeleteView,
    CustomerEditView,
    ProductView,
    ProductCreateView,
    ProductDetailView,
    ProductDeleteView,
    ProductUpdateView,
    AdsView,
    AdsCreateView,
    AdsDetailView,
    AdsDeleteView,
    AdsUpdateView,
    AdsStatListView,
    ContractView,
    ContractCreateView,
    ContractDetailView,
    ContractDeleteView,
    ContractUpdateView,
)

app_name: str = "office"

urlpatterns: list = [
    path('stat/', OfficeStatView.as_view(), name='index'),
    path('leads/', LeadView.as_view(), name='leads'),
    path('leads/<int:pk>', LeadDetailView.as_view(), name='detail-lead'),
    path('leads/new/', LeadCreateView.as_view(), name='create-lead'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='delete-lead'),
    path('leads/<int:pk>/edit/', LeadUpdateView.as_view(), name='edit-lead'),
    path('customers/<int:pk>/add_customer/', LeadToCustomerView.as_view(), name='lead-to-customer'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('customers/new/', CustomerCreateView.as_view(), name='create-customers'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='detail-customer'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete-customer'),
    path('customers/<int:pk>/edit/', CustomerEditView.as_view(), name='edit-customer'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/new/', ProductCreateView.as_view(), name='create-product'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='detail-product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete-product'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit-product'),
    path('ads/', AdsView.as_view(), name='ads'),
    path('ads/new/', AdsCreateView.as_view(), name='create-ad'),
    path('ads/<int:pk>', AdsDetailView.as_view(), name='detail-ad'),
    path('ads/<int:pk>/delete/', AdsDeleteView.as_view(), name='delete-ad'),
    path('ads/<int:pk>/edit/', AdsUpdateView.as_view(), name='edit-ad'),
    path('ads/statistic/', AdsStatListView.as_view(), name='stat-ads'),
    path('contracts/', ContractView.as_view(), name='contracts'),
    path('contracts/new/', ContractCreateView.as_view(), name='create-contract'),
    path('contracts/<int:pk>', ContractDetailView.as_view(), name='detail-contract'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='delete-contract'),
    path('contracts/<int:pk>/edit/', ContractUpdateView.as_view(), name='edit-contract'),
]
