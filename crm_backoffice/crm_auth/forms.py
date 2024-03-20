"""Модуль с формой для аутентификации пользователя"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


ATTRS_USER: dict[str, str] = {"type": "text", "class": "form-control mb-4"}


class UserLoginForm(AuthenticationForm):
    """
    Класс для описания формы аутентификации пользователя
    """
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username: UsernameField = UsernameField(widget=forms.TextInput(attrs=ATTRS_USER))
    password: forms.CharField = forms.CharField(widget=forms.PasswordInput(attrs=ATTRS_USER))
