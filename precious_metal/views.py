from django.views.generic import ListView, CreateView, DeleteView
from .models import PreciousMetal
from precious_metal.forms import MetalForm
from django.urls import reverse_lazy


class PreciousMetalHomepage(ListView): #Listview has probably "objectlist" as original function
    model = PreciousMetal
    template_name = "precious_metal/homepage_precious_metal.html" 


class CreateMetal(CreateView):
    # after click on "submit" it redirect to "precious_metal_homepage" because of the method in model "get_absolute_url"
    template_name = "precious_metal/metal_create.html"
    form_class = MetalForm
    model = PreciousMetal


class DeleteMetal(DeleteView):
    # after click on >delete< it redirect to "precious_metal_homepage"
    template_name = "precious_metal/metal_confirm_delete.html"
    model = PreciousMetal
    success_url = reverse_lazy("precious_metal_homepage")
    # extra_context = {"page_name": "Delete metal"}
    
