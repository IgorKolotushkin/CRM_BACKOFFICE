from django import forms

from .models import Ads


class LeadCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(LeadCreateForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"type": "text", "class": "form-control mb-4"}))
    ads = forms.ModelChoiceField(
        widget=forms.Select(attrs={"type": "text", "class": "form-control mb-4"}),
        queryset=Ads.objects.all(),
    )

    def save(self, commit=True):
        session = super(LeadCreateForm, self).save(commit=False)

        if commit:
            session.save()

        return session
