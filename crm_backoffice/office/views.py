"""Модуль с View для crm."""
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, Sum, QuerySet
from django.http import HttpRequest, HttpResponse, request
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .models import Lead, Customer, Product, Ads, Contract
from .forms import LeadForm, ProductForm, AdsForm, CustomerForm, ContractForm


class OfficeStatView(LoginRequiredMixin, View):
    """View начальной страницы"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Метод для получения статистики по всем категориям.
        """
        context: dict = {
            'products_count': Product.objects.count(),
            'advertisements_count': Ads.objects.count(),
            'leads_count': Lead.objects.count(),
            'customers_count': Customer.objects.count(),
        }
        return render(request, 'users/index.html', context=context)


class CustomerView(PermissionRequiredMixin, ListView):
    """
    View для просмотра всех Customers
    """
    permission_required: str = "office.view_customer"
    template_name: str = "customers/customers-list.html"
    queryset: QuerySet = Customer.objects.all()
    context_object_name: str = "customers"


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Customer
    """
    permission_required: str = "office.add_customer"
    form_class: CustomerForm = CustomerForm
    template_name: str = "customers/customers-create.html"
    success_url = reverse_lazy("office:customers")


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Customer
    """
    permission_required: str = "office.view_customer"
    model: Customer = Customer
    template_name: str = "customers/customers-detail.html"


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Customer
    """
    permission_required: str = "office.delete_customer"
    model: Customer = Customer
    template_name: str = "customers/customers-delete.html"
    success_url = reverse_lazy("office:customers")


class CustomerEditView(PermissionRequiredMixin, UpdateView):
    permission_required = "office.change_customer"
    form_class: CustomerForm = CustomerForm
    template_name: str = "customers/customers-edit.html"
    success_url = reverse_lazy("office:customers")

    def get_success_url(self) -> str:
        """
        Метод для определения URL-адреса для перенаправления при успешной проверке формы
        :return: URL-адрес, на который будет перенаправление после успешной обработки формы.
        """
        return reverse("office:detail-customer", kwargs={"pk": self.object.pk})

    def get_queryset(self) -> Any:
        """
        Переопределенный метод для получения QuerySet с необходимыми свойствами
        :return: QuerySet с необходимыми вам свойствами.
        """
        return Customer.objects.filter(pk=self.kwargs.get('pk'))


class LeadView(PermissionRequiredMixin, ListView):
    """View для просмотра всех Lead."""
    permission_required: str = "office.view_lead"
    template_name: str = "leads/leads-list.html"
    queryset: QuerySet = Lead.objects.select_related("ads")
    context_object_name: str = "leads"


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Lead
    """
    permission_required: str = "office.add_lead"
    form_class: LeadForm = LeadForm
    template_name: str = "leads/leads-create.html"
    success_url = reverse_lazy("office:leads")


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Lead
    """
    permission_required: str = "office.delete_lead"
    model: Lead = Lead
    template_name: str = "leads/leads-delete.html"
    success_url = reverse_lazy("office:leads")


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Lead
    """
    permission_required: str = "office.view_lead"
    model: Lead = Lead
    template_name: str = "leads/leads-detail.html"


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для обновления информации по Lead
    """
    permission_required: str = "office.change_lead"
    form_class: LeadForm = LeadForm
    template_name: str = "leads/leads-edit.html"

    def get_success_url(self) -> str:
        """
        Метод для определения URL-адреса для перенаправления при успешной проверке формы
        :return: URL-адрес, на который будет перенаправление после успешной обработки формы.
        """
        return reverse("office:detail-lead", kwargs={"pk": self.object.pk})

    def get_queryset(self) -> Any:
        """
        Переопределенный метод для получения QuerySet с необходимыми свойствами
        :return: QuerySet с необходимыми вам свойствами.
        """
        return Lead.objects.filter(pk=self.kwargs.get('pk'))


class LeadToCustomerView(PermissionRequiredMixin, CreateView):
    """
    View для перевода потенциального клиента в активного
    """
    permission_required: str = "office.add_lead"
    form_class: CustomerForm = CustomerForm
    template_name: str = "customers/customers-create.html"
    success_url = reverse_lazy("office:customers")

    def get(self, request, *args, **kwargs) -> HttpResponse:
        """Метод для получения предзаполненной формы для перевода lead в customer"""
        lead: Lead = Lead.objects.filter(pk=self.kwargs.get('pk'))
        form: CustomerForm = CustomerForm(initial={'lead': lead[0], })
        return render(request, 'customers/customers-create.html', {'form': form})


class ProductView(PermissionRequiredMixin, ListView):
    """
    View для просмотра всех Product
    """
    permission_required: str = "office.view_product"
    template_name: str = "products/products-list.html"
    queryset: QuerySet = Product.objects.all()
    context_object_name: str = "products"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Product
    """
    permission_required: str = "office.add_product"
    form_class: str = ProductForm
    template_name: str = "products/products-create.html"
    success_url = reverse_lazy("office:products")


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Product
    """
    permission_required: str = "office.delete_product"
    model: Product = Product
    template_name: str = "products/products-delete.html"
    success_url = reverse_lazy("office:products")


class ProductDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации о Product
    """
    permission_required: str = "office.view_product"
    model: Product = Product
    template_name: str = "products/products-detail.html"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для изменении информации о Product
    """
    permission_required: str = "office.change_product"
    form_class: ProductForm = ProductForm
    template_name: str = "products/products-edit.html"

    def get_success_url(self) -> str:
        """
        Метод для определения URL-адреса для перенаправления при успешной проверке формы
        :return: URL-адрес, на который будет перенаправление после успешной обработки формы.
        """
        return reverse("office:detail-product", kwargs={"pk": self.object.pk})

    def get_queryset(self) -> Any:
        """
        Переопределенный метод для получения QuerySet с необходимыми свойствами
        :return: QuerySet с необходимыми вам свойствами.
        """
        return Product.objects.filter(pk=self.kwargs.get('pk'))


class AdsView(PermissionRequiredMixin, ListView):
    """
    View для просмотра всех Ads
    """
    permission_required: str = "office.view_ads"
    template_name: str = "ads/ads-list.html"
    queryset: QuerySet = Ads.objects.select_related('product')
    context_object_name: str = "ads"


class AdsCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Ad
    """
    permission_required: str = "office.add_ads"
    form_class: AdsForm = AdsForm
    template_name: str = "ads/ads-create.html"
    success_url = reverse_lazy("office:ads")


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Ad
    """
    permission_required: str = "office.delete_ads"
    model: Ads = Ads
    template_name: str = "ads/ads-delete.html"
    success_url = reverse_lazy("office:ads")


class AdsDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Ad
    """
    permission_required: str = "office.view_ads"
    model: Ads = Ads
    template_name: str = "ads/ads-detail.html"


class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для обновления информации по Ad
    """
    permission_required: str = "office.change_ads"
    form_class: AdsForm = AdsForm
    template_name: str = "ads/ads-edit.html"

    def get_success_url(self) -> str:
        """
        Метод для определения URL-адреса для перенаправления при успешной проверке формы
        :return: URL-адрес, на который будет перенаправление после успешной обработки формы.
        """
        return reverse("office:detail-ad", kwargs={"pk": self.object.pk})

    def get_queryset(self) -> Any:
        """
        Переопределенный метод для получения QuerySet с необходимыми свойствами
        :return: QuerySet с необходимыми вам свойствами.
        """
        return Ads.objects.filter(pk=self.kwargs.get('pk'))


class AdsStatListView(PermissionRequiredMixin, View):
    """
    View для просмотра статистики по рекламным компаниям
    """
    permission_required: str = "office.view_ads"

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Метод ля получения статистики успешности рекламных компаний
        :param request: request
        :return: статистики
        """
        context: dict = {
            'ads': [
                {
                    'pk': ad.pk,
                    'name': ad.name,
                    'leads_count': ad.lead_set.count(),
                    'customers_count': ad.lead_set.aggregate(cust_count=Count('customer'))['cust_count'],
                    'profit': round(ad.lead_set.aggregate(
                        profit=(Sum('customer__contract__cost') / Sum('ads__budget')) * 100)['profit'], 1),
                } for ad in Ads.objects.all()
            ],
        }
        return render(request, 'ads/ads-statistic.html', context=context)


class ContractView(PermissionRequiredMixin, ListView):
    """
    View для просмотра всех Contracts
    """
    permission_required: str = "office.view_contract"
    template_name: str = "contracts/contracts-list.html"
    queryset: QuerySet = Contract.objects.all()
    context_object_name: str = "contracts"


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Contract
    """
    permission_required: str = "office.add_contract"
    form_class: ContractForm = ContractForm
    template_name: str = "contracts/contracts-create.html"
    success_url = reverse_lazy("office:contracts")


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Contract
    """
    permission_required: str = "office.delete_contract"
    model: Contract = Contract
    template_name: str = "contracts/contracts-delete.html"
    success_url = reverse_lazy("office:contracts")


class ContractDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Contract
    """
    permission_required: str = "office.view_contract"
    model: Contract = Contract
    template_name: str = "contracts/contracts-detail.html"


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для обновления информации о Contract
    """
    permission_required: str = "office.change_contract"
    form_class: ContractForm = ContractForm
    template_name: str = "contracts/contracts-edit.html"

    def get_success_url(self) -> str:
        """
        Метод для определения URL-адреса для перенаправления при успешной проверке формы
        :return: URL-адрес, на который будет перенаправление после успешной обработки формы.
        """
        return reverse("office:detail-contract", kwargs={"pk": self.object.pk})

    def get_queryset(self) -> Any:
        """
        Переопределенный метод для получения QuerySet с необходимыми свойствами
        :return: QuerySet с необходимыми вам свойствами.
        """
        return Contract.objects.filter(pk=self.kwargs.get('pk'))
