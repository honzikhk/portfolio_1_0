from django.views.generic import ListView, CreateView, DeleteView
from .models import Cryptocurrency
from django.urls import reverse_lazy
from .forms import CryptocurrencyForm


class CryptocurrenciesHomepage(ListView):
    model = Cryptocurrency
    template_name = "cryptocurrencies/homepage_cryptocurrencies.html"


class CryptocurrencyCreate(CreateView):
    model = Cryptocurrency
    template_name = "cryptocurrencies/cryptocurrency_create.html"
    form_class = CryptocurrencyForm

class CryptocurrencyDelete(DeleteView):
    model = Cryptocurrency
    template_name = "cryptocurrencies/cryptocurrency_confirm_delete.html"
    success_url = reverse_lazy("homepage_cryptocurrencies")