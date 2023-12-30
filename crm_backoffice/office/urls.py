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
)

app_name = "office"

urlpatterns = [
    path('stat/', OfficeStatView.as_view(), name='index'),
    path('leads/', LeadView.as_view(), name='leads'),
    path('leads/<int:pk>', LeadDetailView.as_view(), name='detail-lead'),
    path('leads/new/', LeadCreateView.as_view(), name='create-lead'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='delete-lead'),
    path('leads/<int:pk>/edit/', LeadUpdateView.as_view(), name='edit-lead'),

    # path('customers/', CustomerView.as_view(), name='customers'),
    # path('customers/new/', CustomerCreateView.as_view(), name='create-customers')
]