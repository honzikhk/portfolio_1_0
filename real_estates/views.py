from django.views.generic import ListView, CreateView, DeleteView
from .models import RealEstate
from .forms import RealEstateForm


class RealEstatesHomepage(ListView):
    model = RealEstate
    template_name = "real_estates/homepage_real_estates.html"


class RealEstateCreate(CreateView):
    model = RealEstate
    template_name = "real_estates/real_estate_create.html"
    form_class = RealEstateForm