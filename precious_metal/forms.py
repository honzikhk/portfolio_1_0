from django import forms
from precious_metal.models import PreciousMetal

class MetalForm(forms.ModelForm):
    
    class Meta:
        model = PreciousMetal
        exclude = ["created"] 
