from django.urls import path
from .views import CryptocurrenciesHomepage

urlpatterns = [
    path("", CryptocurrenciesHomepage.as_view(), name="homepage_cryptocurrencies"),
    
]