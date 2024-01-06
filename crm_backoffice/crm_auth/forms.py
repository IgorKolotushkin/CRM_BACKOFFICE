from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
