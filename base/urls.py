from django.urls import path
from .views import BaseHomepageView

urlpatterns = [
    path("", BaseHomepageView.as_view(), name="base_homepage"),
]