from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CrmLoginView(LoginView):
    template_name = "registration/login.html"
    next_page = reverse_lazy("office:index")
