from django.views.generic import ListView, CreateView
from .models import PreciousMetal
from precious_metal.forms import MetalForm

class PreciousMetalHomepage(ListView):
    model = PreciousMetal
    template_name = "precious_metal/homepage_precious_metal.html" #try to remove "precious_metal/"


class CreateMetal(CreateView):
    # after click on "submit" it redirect to "precious_metal_homepage" because of the method in model "get_absolute_url"
    template_name = "precious_metal/metal_create.html"  #try to remove "precious_metal/"
    form_class = MetalForm
    model = PreciousMetal
    
