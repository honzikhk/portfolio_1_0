from django.urls import path
from .views import RealEstatesHomepage

urlpatterns = [
    path("", RealEstatesHomepage.as_view(), name="real_estates_homepage"),
]