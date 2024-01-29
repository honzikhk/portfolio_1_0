from django.views.generic import ListView, CreateView, DeleteView
from .models import Cash
from .forms import CashForm
from django.urls import reverse_lazy

class CashHomepage(ListView):
    model = Cash
    template_name = "cash/homepage_cash.html"


class CashCreate(CreateView):
    model = Cash
    template_name = "cash/cash_create.html"
    form_class = CashForm


class CashDelete(DeleteView):
    model = Cash
    template_name = "cash/cash_confirm_delete.html"
    success_url = reverse_lazy("cash_homepage")