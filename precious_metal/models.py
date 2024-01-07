from django.db import models


class PreciousMetal(models.Model):
    # id field is added automatically
    item = models.CharField(max_length=30)
    value = models.IntegerField()
    note = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item        # represent objects by their names in admin page