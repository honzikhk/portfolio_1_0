from django import forms
from .models import RealEstate

class RealEstateForm(forms.ModelForm):

    class Meta:
        model = RealEstate
        exclude = ["created"]