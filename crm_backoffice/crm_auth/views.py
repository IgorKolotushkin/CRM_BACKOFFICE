"""Модуль с View для login пользователя """
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import UserLoginForm


class CrmLoginView(LoginView):
    """
    Класс для отображения страницы и формы аутентификации пользователя
    """
    authentication_form: UserLoginForm = UserLoginForm
    template_name: str = "registration/login.html"
    next_page = reverse_lazy("office:index")
