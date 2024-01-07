from django.views.generic import ListView
from .models import PreciousMetal

class PreciousMetalHomepage(ListView):
    model = PreciousMetal
    template_name = "precious_metal/homepage_precious_metal.html"
