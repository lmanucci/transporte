from dataclasses import field, fields
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.forms import ChoiceWidget, ModelForm
from django.contrib.auth.models import User

class viajesformulario (forms.Form):
    Facturación = forms.CharField (max_length=30)
    Camion= forms.CharField (max_length=30)
    Origen= forms.CharField (max_length=30)
    Mercaderia = forms.CharField (max_length=30)
    Toneladas = forms.IntegerField()
    Tarifa = forms.IntegerField()
    #Documentos = forms.ImageField(required=False)
    
class camioneroformulario (forms.Form):
    Nombre_Completo=forms.CharField (max_length=30)
    Apellido=forms.CharField (max_length=30)

class Entidadesformulario (forms.Form):
    tipoentidad = forms.CharField (max_length=30)
    Documento = forms.IntegerField()
    nombre = forms.CharField (max_length=30)

rol = [("chofer", "Chofer"),("Admin", "Administrador")] 
class UserRegisterForm (UserCreationForm):
    Nombre= forms.CharField(max_length=30,label="Nombre Completo")
    Apellido= forms.CharField(max_length=30,label="Apellido")
    DNI= forms.IntegerField(required=False, label="DNI")
    email=forms.EmailField(label="Correo Electronico")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    roles = forms.MultipleChoiceField(choices=rol, label="Roles", widget=forms.Select(choices=[rol]))
    
    class Meta:
        model = User
        fields = ['username', 'Nombre','Apellido','DNI','email','password1','password2', 'roles']
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
