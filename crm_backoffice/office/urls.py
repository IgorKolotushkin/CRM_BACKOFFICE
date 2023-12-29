from django.urls import path

from .views import OfficeStatView

app_name = "office"

urlpatterns = [
    path('stat/', OfficeStatView.as_view(), name='index'),
]