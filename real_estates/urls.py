from django.urls import path
from .views import RealEstatesHomepage, RealEstateCreate

urlpatterns = [
    path("", RealEstatesHomepage.as_view(), name="real_estates_homepage"),
    path("create_real_estate/", RealEstateCreate.as_view(), name="real_estate_create"),
]