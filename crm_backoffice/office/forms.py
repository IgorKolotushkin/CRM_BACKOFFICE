"""Модуль с формами"""
from django import forms

from .models import Ads, Lead, Product, Customer, Contract

ATTRS_TEXT: dict[str, str] = {"type": "text", "class": "form-control mb-4"}
ATTRS_EMAIL: dict[str, str] = {"type": "text", "class": "form-control mb-4"}
ATTRS_DATE: dict[str, str] = {"type": "date", "class": "form-control mb-4"}
ATTRS_NUMBER: dict[str, str] = {"type": "number", "class": "form-control mb-4"}
ATTRS_FILE: dict[str, str] = {"type": "file", "class": "form-control mb-4"}


class LeadForm(forms.ModelForm):
    """
    Класс с формой для добавления и редактирования потенциального клиента.
    """
    class Meta:
        model: Lead = Lead
        fields: tuple = "first_name", "last_name", "email", "phone", "ads"

        widgets: dict = {
            'first_name': forms.TextInput(attrs=ATTRS_TEXT),
            'last_name': forms.TextInput(attrs=ATTRS_TEXT),
            'email': forms.EmailInput(attrs=ATTRS_EMAIL),
            'phone': forms.TextInput(attrs=ATTRS_TEXT),
            'ads': forms.Select(attrs=ATTRS_TEXT),
        }


class ProductForm(forms.ModelForm):
    """
    Класс с формой для добавления и редактирования продукта.
    """
    class Meta:
        model: Product = Product
        fields: tuple = "name", "description", "cost"

        widgets: dict = {
            'name': forms.TextInput(attrs=ATTRS_TEXT),
            'description': forms.Textarea(attrs=ATTRS_TEXT),
            'cost': forms.NumberInput(attrs=ATTRS_NUMBER),
        }


class AdsForm(forms.ModelForm):
    """
    Класс с формой для добавления и редактирования рекламы.
    """
    class Meta:
        model: Ads = Ads
        fields: tuple = "name", "product", "channel", "budget"

        widgets: dict = {
            'name': forms.TextInput(attrs=ATTRS_TEXT),
            'product': forms.Select(attrs=ATTRS_TEXT),
            'channel': forms.TextInput(attrs=ATTRS_TEXT),
            'budget': forms.NumberInput(attrs=ATTRS_NUMBER),
        }


class CustomerForm(forms.ModelForm):
    """
    Класс с формой для добавления и редактирования активного клиента.
    """
    class Meta:
        model: Customer = Customer
        fields: tuple = "lead", "contract"

        widgets: dict = {
            'lead': forms.Select(attrs=ATTRS_TEXT),
            'contract': forms.Select(attrs=ATTRS_TEXT),
        }


class ContractForm(forms.ModelForm):
    """
    Класс с формой для добавления и редактирования контракта.
    """
    class Meta:
        model: Contract = Contract
        fields: tuple = "name", "product", "start_date", "end_date", "cost", "file"

        widgets: dict = {
            'name': forms.TextInput(attrs=ATTRS_TEXT),
            'start_date': forms.DateInput(attrs=ATTRS_DATE),
            'end_date': forms.DateInput(attrs=ATTRS_DATE),
            'product': forms.Select(attrs=ATTRS_TEXT),
            'cost': forms.NumberInput(attrs=ATTRS_NUMBER),
            'file': forms.FileInput(attrs=ATTRS_FILE),
        }
