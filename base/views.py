from django.views.generic import TemplateView
from precious_metal.models import PreciousMetal
from django.template.response import TemplateResponse


class BaseHomepageView(TemplateView):
    template_name = "base/base_homepage.html"

    def count_sum_of_values(self):      # sum of all values of all metals in USD
        sum = 0
        for metal in PreciousMetal.objects.all():
            sum += metal.value
        return sum

    def get(self, request, *args, **kwargs):    # maybe remove *args, **kwargs
        context = {
            "count_of_items": PreciousMetal.objects.all().count(),      # shows how many items is in precoius metals
            "sum_of_values": self.count_sum_of_values(),
            'page_name': 'Books homepage'   # wtf is that
        }
        return TemplateResponse(request, "base/base_homepage.html", context=context)

