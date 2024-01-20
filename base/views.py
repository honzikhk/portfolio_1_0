from django.views.generic import TemplateView
from precious_metal.models import PreciousMetal
from real_estates.models import RealEstate
from django.template.response import TemplateResponse


class BaseHomepageView(TemplateView):
    template_name = "base/base_homepage.html"

    def count_sum_of_values_precious_metals(self):      # sum of all values of all metals in USD
        sum = 0
        for metal in PreciousMetal.objects.all():
            sum += metal.value
        return sum

    def count_sum_of_values_real_estates(self):
        sum = 0
        for real_estate in RealEstate.objects.all():
            sum += real_estate.value
        return sum

    def get(self, request, *args, **kwargs):    # maybe remove *args, **kwargs
        context = {
            "precious_metals_count_of_items": PreciousMetal.objects.all().count(),      # shows how many items is in precoius metals
            "precious_metals_sum_of_values": self.count_sum_of_values_precious_metals(),
            "real_estates_count_of_items": RealEstate.objects.all().count(),        # shows how many items is in real estates
            "real_estates_sum_of_values": self.count_sum_of_values_real_estates(),
            #"value_of_all_assets": 

        }
        return TemplateResponse(request, "base/base_homepage.html", context=context)

