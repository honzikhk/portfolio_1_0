from django.views.generic import ListView, CreateView
from .models import Cash
from .forms import CashForm

class CashHomepage(ListView):
    model = Cash
    template_name = "cash/homepage_cash.html"


class CashCreate(CreateView):
    model = Cash
    template_name = "cash/cash_create.html"
    form_class = CashForm