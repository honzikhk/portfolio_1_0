from django import forms
from .models import Cryptocurrency

class CryptocurrencyForm(forms.ModelForm):
    
    class Meta:
        model = Cryptocurrency
        exclude = ["created"]