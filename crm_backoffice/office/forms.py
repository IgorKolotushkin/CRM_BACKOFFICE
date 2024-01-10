from django import forms

from .models import Ads, Lead, Product, Customer, Contract

ATTRS_TEXT = {"type": "text", "class": "form-control mb-4"}
ATTRS_EMAIL = {"type": "text", "class": "form-control mb-4"}
ATTRS_DATE = {"type": "date", "class": "form-control mb-4"}
ATTRS_NUMBER = {"type": "number", "class": "form-control mb-4"}
ATTRS_FILE = {"type": "file", "class": "form-control mb-4"}


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "first_name", "last_name", "email", "phone", "ads"

        widgets = {
            'first_name': forms.TextInput(attrs=ATTRS_TEXT),
            'last_name': forms.TextInput(attrs=ATTRS_TEXT),
            'email': forms.EmailInput(attrs=ATTRS_EMAIL),
            'phone': forms.TextInput(attrs=ATTRS_TEXT),
            'ads': forms.Select(attrs=ATTRS_TEXT),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "cost"

        widgets = {
            'name': forms.TextInput(attrs=ATTRS_TEXT),
            'description': forms.Textarea(attrs=ATTRS_TEXT),
            'cost': forms.NumberInput(attrs=ATTRS_NUMBER),
        }


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = "name", "product", "channel", "budget"

        widgets = {
            'name': forms.TextInput(attrs=ATTRS_TEXT),
            'product': forms.Select(attrs=ATTRS_TEXT),
            'channel': forms.TextInput(attrs=ATTRS_TEXT),
            'budget': forms.NumberInput(attrs=ATTRS_NUMBER),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "lead", "contract"

        widgets = {
            'lead': forms.Select(attrs=ATTRS_TEXT),
            'contract': forms.Select(attrs=ATTRS_TEXT),
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "name", "product", "start_date", "end_date", "cost", "file"

        widgets = {
            'name': forms.TextInput(attrs=ATTRS_TEXT),
            'start_date': forms.DateInput(attrs=ATTRS_DATE),
            'end_date': forms.DateInput(attrs=ATTRS_DATE),
            'product': forms.Select(attrs=ATTRS_TEXT),
            'cost': forms.NumberInput(attrs=ATTRS_NUMBER),
            'file': forms.FileInput(attrs=ATTRS_FILE),
        }
