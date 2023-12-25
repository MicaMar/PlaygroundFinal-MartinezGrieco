from django import forms
from .models import *

class AdministradorAccesorios(forms.Form):
    producto = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    
    
class AdministradorTextiles(forms.Form):
    producto = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)

class ConsultaFormulario(forms.ModelForm)  :
    class Meta:
        model = ConsultaFormulario
        fields = ("__all__")