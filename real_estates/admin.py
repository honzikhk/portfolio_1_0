from django.contrib import admin
from .models import RealEstate


class RealEstateAdmin(admin.ModelAdmin):
    list_display = ("item", "value")
    list_filter = ("created", )

admin.site.register(RealEstate, RealEstateAdmin)
