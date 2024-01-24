from django.views.generic import ListView
from .models import Cryptocurrency


class CryptocurrenciesHomepage(ListView):
     model = Cryptocurrency
     template_name = "cryptocurrencies/homepage_cryptocurrencies.html"