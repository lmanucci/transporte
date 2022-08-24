from dataclasses import field, fields
from distutils.command import upload
from enum import auto
#from lzma import _FilterChain
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from xmlrpc.client import DateTime
from django import forms
from django.forms import ModelForm, ClearableFileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.forms import ChoiceWidget, ModelForm
from django.contrib.auth.models import User
#from ProyectoOrdenesCarga.app_Misviajes.models import Localidades, Vehiculos
from app_Misviajes.models import Entidades, Viajes, Localidades, Vehiculos

#class viajesformulario (forms.Form):
 #   Fecha = forms.DateField()
  #  Cliente = forms.ChoiceField(choices=[Entidades], required=False)
   # #Facturación = forms.CharField (max_length=30)
    #tipdoc = ((1,"C.T.G"),(2,"Remito"))
    #Tipodoc = forms.ChoiceField(choices= tipdoc)
    #Documento = forms.CharField(max_length=10)
    #Listkm= ((1,"50"),(2,"100"),(3,"150"),(4,"200"),(5,"250"),(6,"300"),(7,"350"),(8,"400"),(9,"450"),(10,"500"),(11,"550"),(12,"600"),(13,"650"),(14,"700"),(15,"750"),(16,"800"))
    #Kilometros = forms.ChoiceField(choices=  Listkm)
    #Camion= forms.ChoiceField(choices=[Vehiculos], required=False)
    #Origen= forms.ChoiceField(choices=[Localidades], required=False)
    #Mercaderia = forms.CharField (max_length=30)
    #Toneladas = forms.DecimalField(max_digits=5, decimal_places=2)
    #Tarifa = forms.DecimalField(max_digits=7, decimal_places=2)
    #Documentación = forms.FileField()
    
    #def importe (self):
        #return (self.Toneladas * self.Tarifa)
class DateInput(forms.DateInput):
    input_type= 'date' 

class viajesformulario (ModelForm):
    class Meta:
        model = Viajes
        exclude = ['Facturado', 'Fecha_Factura', 'Nro_Factura']
        fields= "__all__"
        widgets = {'Fecha':DateInput(attrs={'class': 'form-control'})}
        

class facturar (ModelForm):
    class Meta:
        model = Viajes
        exclude = ['Documentación']
        fields= "__all__"

    
class vehiculosformulario (forms.Form):
    Tipo_Veh = ((1,"Camion"),(2,"Acoplado"))
    Vehiculo =forms.ChoiceField(choices=Tipo_Veh)
    Patente = forms.CharField (max_length=7)
    DescripVeh = forms.CharField (max_length=30, label= "Descripción de Vehiculo")    


class camioneroformulario (forms.Form):
    Nombre_Completo=forms.CharField (max_length=30)
    Apellido=forms.CharField (max_length=30)

class Entidadesformulario (ModelForm):
    class Meta:
        model = Entidades
        fields= "__all__"
    
    #Tipos = ((1,"Camioneros"),(2,"Cliente"))
    #tipoentidad = forms.PositiveSmallIntegerField("Tipo_Entidad", choices=Tipos)
    #Documento = forms.IntegerField()
    #nombre = forms.CharField (max_length=30)

#rol = [("chofer", "Chofer"),("Admin", "Administrador")] 
class UserRegisterForm (UserCreationForm):
    Nombre= forms.CharField(max_length=30,label="Nombre Completo")
    Apellido= forms.CharField(max_length=30,label="Apellido")
    DNI= forms.IntegerField(required=False, label="DNI")
    email=forms.EmailField(label="Correo Electronico")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    #roles = forms.MultipleChoiceField(choices=rol, label="Roles", widget=forms.Select(choices=[rol]))
    
    class Meta:
        model = User
        fields = ['username', 'Nombre','Apellido','DNI','email','password1','password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Correo Electronico")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    Nombre= forms.CharField(max_length=30,label="Nombre Completo")
    Apellido= forms.CharField(max_length=30,label="Apellido")

    class Meta:
        model = User
        fields = ['email','password1','password2', 'Nombre','Apellido']
        help_texts = {k: "" for k in fields}
