from django.views.generic import ListView, CreateView, DeleteView
from .models import RealEstate
from .forms import RealEstateForm
from django.urls import reverse_lazy

class RealEstatesHomepage(ListView):
    model = RealEstate
    template_name = "real_estates/homepage_real_estates.html"


class RealEstateCreate(CreateView):
    model = RealEstate
    template_name = "real_estates/real_estate_create.html"
    form_class = RealEstateForm


class RealEstateDelete(DeleteView):
    model = RealEstate
    template_name = "real_estates/real_estate_confirm_delete.html"
    success_url = reverse_lazy("real_estates_homepage")