from django.urls import path
from .views import PreciousMetalHomepage, CreateMetal, DeleteMetal

urlpatterns = [
    path("", PreciousMetalHomepage.as_view(), name="precious_metal_homepage"),
    path("create_metal/", CreateMetal.as_view(), name="metal_create"),
    path("delete_metal/<int:pk>/", DeleteMetal.as_view(), name="metal_delete"),        #write something like <int:pk> to display what metal gonna delete
]