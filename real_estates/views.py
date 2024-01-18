from django.views.generic import ListView
from .models import RealEstate


class RealEstatesHomepage(ListView):
    model = RealEstate
    template_name = "real_estates/homepage_real_estates.html"