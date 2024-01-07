from django.urls import path
from .views import PreciousMetalHomepage

urlpatterns = [
    path("", PreciousMetalHomepage.as_view(), name="precious_metal_homepage"),
]