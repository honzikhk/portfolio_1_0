from django.contrib import admin
from .models import PreciousMetal


class PreciousMetalAdmin(admin.ModelAdmin):
    list_display = ("item", "value")
    list_filter = ("created", )     # here must be "," because it must be tuple 


admin.site.register(PreciousMetal, PreciousMetalAdmin)
