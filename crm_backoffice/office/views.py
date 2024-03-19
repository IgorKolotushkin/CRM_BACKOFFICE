"""Модуль с View."""
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, Sum
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
    permission_required = "office.view_customer"
    template_name = "customers/customers-list.html"
    queryset = Customer.objects.all()
    context_object_name = "customers"


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Customer
    """
    permission_required = "office.add_customer"
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("office:customers")


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Customer
    """
    permission_required = "office.view_customer"
    model = Customer
    template_name = "customers/customers-detail.html"


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Customer
    """
    permission_required = "office.delete_customer"
    model = Customer
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("office:customers")


class CustomerEditView(UpdateView):
    # permission_required = "office.add_customer"
    form_class = CustomerForm
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy("office:customers")

    def get_success_url(self):
        return reverse("office:detail-customer", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Customer.objects.filter(pk=self.kwargs.get('pk'))


class LeadView(PermissionRequiredMixin, ListView):
    """View для просмотра всех Lead."""
    permission_required = "office.view_lead"
    template_name = "leads/leads-list.html"
    queryset = Lead.objects.select_related("ads")
    context_object_name = "leads"


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Lead
    """
    permission_required = "office.add_lead"
    form_class = LeadForm
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("office:leads")


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Lead
    """
    permission_required = "office.delete_lead"
    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("office:leads")


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Lead
    """
    permission_required = "office.view_lead"
    model = Lead
    template_name = "leads/leads-detail.html"


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для обновления информации по Lead
    """
    permission_required = "office.change_lead"
    form_class = LeadForm
    template_name = "leads/leads-edit.html"

    def get_success_url(self):
        return reverse("office:detail-lead", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Lead.objects.filter(pk=self.kwargs.get('pk'))


class LeadToCustomerView(CreateView):  # PermissionRequiredMixin,
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("office:customers")

    def get(self, request, *args, **kwargs):
        lead = Lead.objects.filter(pk=self.kwargs.get('pk'))
        form = CustomerForm(initial={'lead': lead[0], })
        return render(request, 'customers/customers-create.html', {'form': form})


class ProductView(PermissionRequiredMixin, ListView):
    """
    View для просмотра всех Product
    """
    permission_required = "office.view_product"
    template_name = "products/products-list.html"
    queryset = Product.objects.all()
    context_object_name = "products"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Product
    """
    permission_required = "office.add_product"
    form_class = ProductForm
    template_name = "products/products-create.html"
    success_url = reverse_lazy("office:products")


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Product
    """
    permission_required = "office.delete_product"
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("office:products")


class ProductDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации о Product
    """
    permission_required = "office.view_product"
    model = Product
    template_name = "products/products-detail.html"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для изменении информации о Product
    """
    permission_required = "office.change_product"
    form_class = ProductForm
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return reverse("office:detail-product", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs.get('pk'))


class AdsView(PermissionRequiredMixin, ListView):
    """
    View для просмотра всех Ads
    """
    permission_required = "office.view_ads"
    template_name = "ads/ads-list.html"
    queryset = Ads.objects.select_related('product')
    context_object_name = "ads"


class AdsCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Ad
    """
    permission_required = "office.add_ads"
    form_class = AdsForm
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("office:ads")


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Ad
    """
    permission_required = "office.delete_ads"
    model = Ads
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("office:ads")


class AdsDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Ad
    """
    permission_required = "office.view_ads"
    model = Ads
    template_name = "ads/ads-detail.html"


class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для обновления информации по Ad
    """
    permission_required = "office.change_ads"
    form_class = AdsForm
    template_name = "ads/ads-edit.html"

    def get_success_url(self):
        return reverse("office:detail-ad", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Ads.objects.filter(pk=self.kwargs.get('pk'))


class AdsStatListView(View):
    """
    View для просмотра статистики по рекламным компаниям
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
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
    permission_required = "office.view_contract"
    template_name = "contracts/contracts-list.html"
    queryset = Contract.objects.all()
    context_object_name = "contracts"


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """
    View для создания Contract
    """
    permission_required = "office.add_contract"
    form_class = ContractForm
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("office:contracts")


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View для удаления Contract
    """
    permission_required = "office.delete_contract"
    model = Contract
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("office:contracts")


class ContractDetailView(PermissionRequiredMixin, DetailView):
    """
    View для просмотра детальной информации по Contract
    """
    permission_required = "office.view_contract"
    model = Contract
    template_name = "contracts/contracts-detail.html"


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View для обновления информации о Contract
    """
    permission_required = "office.change_contract"
    form_class = ContractForm
    template_name = "contracts/contracts-edit.html"

    def get_success_url(self):
        return reverse("office:detail-contract", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Contract.objects.filter(pk=self.kwargs.get('pk'))
