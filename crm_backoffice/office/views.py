from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class OfficeStatView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'users/index.html', context=context)
