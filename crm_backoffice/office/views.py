from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .models import Lead, Customer


class OfficeStatView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'users/index.html', context=context)


class CustomerView(ListView):
    template_name = "customers/customers-list.html"
    queryset = Customer.objects.all()
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    model = Customer
    fields = "name", "email", "phone"
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("office:customers")


class LeadView(ListView):
    template_name = "leads/leads-list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadCreateView(CreateView):
    model = Lead
    fields = "first_name", "last_name", "email", "phone"
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
    fields = "first_name", "last_name", "email", "phone"

    def get_success_url(self):
        return reverse("office:detail-lead", kwargs={"pk": self.object.pk})
