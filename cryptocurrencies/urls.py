from django.urls import path
from .views import CryptocurrenciesHomepage, CryptocurrencyCreate, CryptocurrencyDelete

urlpatterns = [
    path("", CryptocurrenciesHomepage.as_view(), name="homepage_cryptocurrencies"),
    path("create_cryptocurrency", CryptocurrencyCreate.as_view(), name="cryptocurrency_create"),
    path("delete_cryptocurrency/<int:pk>", CryptocurrencyDelete.as_view(), name="cryptocurrency_delete"),
]