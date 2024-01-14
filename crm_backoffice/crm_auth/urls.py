from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import CrmLoginView

app_name = "crm_auth"

urlpatterns = [
    path('', CrmLoginView.as_view(), name='login'),
    path('', LogoutView.as_view(
        next_page=reverse_lazy('crm_auth:login')
    ), name='logout')
]
