from django import forms
from .models import Cash


class CashForm(forms.ModelForm):

    class Meta:
        model = Cash
        exclude = ["created"]