from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import UserLoginForm


class CrmLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "registration/login.html"
    next_page = reverse_lazy("office:index")
