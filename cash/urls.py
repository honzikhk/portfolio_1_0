from django.urls import path
from .views import CashHomepage, CashCreate, CashDelete

urlpatterns = [
    path("", CashHomepage.as_view(), name="cash_homepage"),
    path("create_cash/", CashCreate.as_view(), name="cash_create" ),
    path("delete_cash/<int:pk>", CashDelete.as_view(), name="cash_delete"),
]