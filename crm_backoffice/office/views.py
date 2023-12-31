from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .models import Lead, Customer, Product, Ads


class OfficeStatView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'products_count': Product.objects.count(),
            'advertisements_count': Ads.objects.count(),
            'leads_count': Lead.objects.count(),
            'customers_count': Customer.objects.count(),
        }
        return render(request, 'users/index.html', context=context)


class CustomerView(ListView):
    template_name = "customers/customers-list.html"
    queryset = Customer.objects.all()
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    queryset = Customer.objects.select_related("lead")
    fields = ["lead", ]
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("office:customers")


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customers-detail.html"


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("office:customers")


class LeadView(ListView):
    template_name = "leads/leads-list.html"
    queryset = Lead.objects.select_related("ads")
    context_object_name = "leads"


class LeadCreateView(CreateView):
    model = Lead
    fields = "first_name", "last_name", "email", "phone", "ads"
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("office:leads")


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("office:leads")


class LeadDetailView(DetailView):
    model = Lead
    template_name = "leads/leads-detail.html"


class LeadUpdateView(UpdateView):
    model = Lead
    template_name = "leads/leads-edit.html"
    fields = "first_name", "last_name", "email", "phone", "ads"

    def get_success_url(self):
        return reverse("office:detail-lead", kwargs={"pk": self.object.pk})


class ProductView(ListView):
    template_name = "products/products-list.html"
    queryset = Product.objects.all()
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "description", "cost"
    template_name = "products/products-create.html"
    success_url = reverse_lazy("office:products")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("office:products")


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/products-detail.html"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/products-edit.html"
    fields = "name", "description", "cost"

    def get_success_url(self):
        return reverse("office:detail-product", kwargs={"pk": self.object.pk})


class AdsView(ListView):
    template_name = "ads/ads-list.html"
    queryset = Ads.objects.select_related('product')
    context_object_name = "ads"


class AdsCreateView(CreateView):
    model = Ads
    fields = "name", "product", "channel", "budget"
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("office:ads")


class AdsDeleteView(DeleteView):
    model = Ads
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("office:ads")


class AdsDetailView(DetailView):
    model = Ads
    template_name = "ads/ads-detail.html"


class AdsUpdateView(UpdateView):
    model = Ads
    template_name = "ads/ads-edit.html"
    fields = "name", "product", "channel", "budget"

    def get_success_url(self):
        return reverse("office:detail-ad", kwargs={"pk": self.object.pk})


# class AdsStatListView(ListView):
#     template_name = "ads/ads-statistic.html"
#     queryset = Ads.objects.all()
#     context_object_name = "ads"


class AdsStatListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        a = Ads.objects.first()
        print(a.lead_set.first().customer_set.count())
        context = {
            'ads': [
                {
                    'pk': ad.pk,
                    'name': ad.name,
                    'leads_count': ad.lead_set.count(),
                } for ad in Ads.objects.all()
            ],
        }
        return render(request, 'ads/ads-statistic.html', context=context)
