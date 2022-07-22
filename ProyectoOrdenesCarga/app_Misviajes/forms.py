from django import forms
from django.forms import ModelForm

class viajesformulario (forms.Form):
    Facturación = forms.CharField (max_length=30)
    Camion= forms.CharField (max_length=30)
    Origen= forms.CharField (max_length=30)
    Mercaderia = forms.CharField (max_length=30)
    Toneladas = forms.IntegerField()
    Tarifa = forms.IntegerField()
    
class camioneroformulario (forms.Form):
    Nombre_Completo=forms.CharField (max_length=30)
    Apellido=forms.CharField (max_length=30)

class Entidadesformulario (forms.Form):
    tipoentidad = forms.CharField (max_length=30)
    Documento = forms.IntegerField()
    nombre = forms.CharField (max_length=30)