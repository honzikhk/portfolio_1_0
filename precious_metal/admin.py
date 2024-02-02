from django.contrib import admin
from .models import PreciousMetal


class PreciousMetalAdmin(admin.ModelAdmin):
    list_display = ("item", "value")    # values displayed id /admin page
    list_filter = ("created", )     # here must be ",". 


admin.site.register(PreciousMetal, PreciousMetalAdmin)
