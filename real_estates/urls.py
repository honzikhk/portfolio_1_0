from django.urls import path
from .views import RealEstatesHomepage, RealEstateCreate, RealEstateDelete

urlpatterns = [
    path("", RealEstatesHomepage.as_view(), name="real_estates_homepage"),
    path("create_real_estate/", RealEstateCreate.as_view(), name="real_estate_create"),
    path("delete_real_estate/<int:pk>", RealEstateDelete.as_view(), name="real_estate_delete"),
]