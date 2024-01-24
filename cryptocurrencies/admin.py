from django.contrib import admin
from .models import Cryptocurrency


class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ("item", "value")
    list_filter = ("created", )


admin.site.register(Cryptocurrency, CryptocurrencyAdmin)