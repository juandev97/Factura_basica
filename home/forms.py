from django import forms
from .models import Persona, item, Factura


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'



class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'



class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
