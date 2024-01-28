from django.contrib import admin
from .models import Cash


class CashAdmin(admin.ModelAdmin):
    list_display = ("item", "value")
    list_filter = ("created", )


admin.site.register(Cash, CashAdmin)
