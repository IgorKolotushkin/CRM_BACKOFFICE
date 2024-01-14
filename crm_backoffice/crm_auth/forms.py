from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type": "text", "class": "form-control mb-4"}))
