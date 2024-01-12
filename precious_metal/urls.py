from django.urls import path
from .views import PreciousMetalHomepage, CreateMetal

urlpatterns = [
    path("", PreciousMetalHomepage.as_view(), name="precious_metal_homepage"),
    path("create_metal/", CreateMetal.as_view(), name="metal_create"),
]