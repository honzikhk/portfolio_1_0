from django.views.generic import TemplateView


class BaseHomepageView(TemplateView):
    template_name = "base/base_homepage.html"
