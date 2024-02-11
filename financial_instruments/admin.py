from django.contrib import admin
from .models import FinancialInstruments


class FinancialInstrumentsAdmin(admin.ModelAdmin):
    list_display = ("item", "value")
    list_filter = ("created", )

admin.site.register(FinancialInstruments, FinancialInstrumentsAdmin)

