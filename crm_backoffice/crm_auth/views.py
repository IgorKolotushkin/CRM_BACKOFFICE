from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import UserLoginForm


class CrmLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"
    next_page = reverse_lazy("office:index")
