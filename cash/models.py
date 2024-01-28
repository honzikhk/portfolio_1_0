from django.db import models
from django.shortcuts import resolve_url

class Cash(models.Model):
    # id field is added automatically
    item = models.CharField(max_length=30)
    value = models.IntegerField()
    note = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item        # represent objects by their names in admin page. also can be used fstring

    def get_absolute_url(self):     # this method redirect to "precious_metal_homepage" after click submit
        return resolve_url("cash_homepage")