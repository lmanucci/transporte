
from dataclasses import field
from pdb import post_mortem
from sre_constants import SUCCESS
from urllib.robotparser import RequestRate
from django.db import models
from django import forms
from urllib import request, response
from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
import http
from django.db.models import Q  #Para poder filtrar por varias variables
from re import template
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from turtle import onclick
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.template import Context, Template
from ProyectoOrdenesCarga import app_Misviajes
from app_Misviajes.models import *
from app_Misviajes.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

#Misma funcionalidad:
#LoginRequiredMixin ----->Restringe acceso para clases
#login_required  ----> Restringe Acceso para funciones
#staff_member_required ----> Restringe a solo administradores

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect ("inicio")
            else:
                return redirect ("login")
        else:
            return redirect ("login")
    form = AuthenticationForm()
    return render (request, "login.html", {"form":form})

def register_request(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password1')#es la primer contraseña, no la confirmación
            #email = form.cleaned_data.get('Correo')
            form.save()
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect ("login")
        return render (request, "register.html",{"form":form})
    #form = UserCreationForm()
    form = UserRegisterForm
    return render(request,"register.html",{"form":form})

def logout_request (request):
    logout(request)
    return redirect ("inicio")


def editar_perfil (request):
    user = request.user #Usuario con el que estamos logueados
    if request.method == "POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user.email = info["email"]
            #user.Nombre = info["Nombre"]
            #user.Apellido = info["Apellido"]
            #user.save()
            return redirect ("inicio")
        return render(request, "editar_perfil.html",{"form":form})
    else:
        form = UserEditForm(initial={"email":user.email})
    return render(request, "editar_perfil.html",{"form":form})

def INICIO (request):
    
    return render (request, "index.html")


@login_required
def entidades (request):
    return render (request,"entidades.html")
@login_required
def localidades (request):
    listado=""
    return render (request,"localidades.html", listado)

@staff_member_required
def vehiculos (request):
    Lista_Vehiculos= Vehiculos.objects.all
    Datos1= {"Lista_Vehiculos":Lista_Vehiculos}
    return render (request,"vehiculos.html",Datos1)

@login_required
def CONSULTAENTIDADES (request):
    Lista_Entidades = Entidades.objects.all()
    ctx= {"Listadoentidades":Lista_Entidades}
    return render (request,"consultaentidades.html", ctx)

@login_required
def Viajesrealizadas (request):
    Lista_Viajes = Viajes.objects.all()
    Chofer = "Lautaro Manucci"
    ctx= {"ListaViajes":Lista_Viajes, "Chofer":Chofer}
    return render (request,"consulviajes.html", ctx) 

@login_required
def Viajesformulario(request):
#Metodo Simplificado    
    if request.method == 'POST':
        info_formulario = viajesformulario(request.POST)
        print(info_formulario)
        if info_formulario.is_valid():
            infofor=info_formulario.cleaned_data
            carga= Viajes (Facturación=infofor['Facturación'],
                           Camion=infofor['Camion'], 
                           Origen=infofor['Origen'], 
                           Mercaderia=infofor['Mercaderia'], 
                           Toneladas=infofor['Toneladas'], 
                           Tarifa=infofor['Tarifa'])
            carga.save()
            return redirect ("consultaviajes") #pagina a donde lo envio al usuario una vez que guarde los datos
        return render(request, "formviajes.html",{"info_formulario":info_formulario})    
    else: #Metodo get
        info_formulario=viajesformulario()
        return render(request, "formviajes.html",{"info_formulario":info_formulario})

@login_required
def Entidadesformularios(request):
#Metodo Simplificado    
    if request.method == 'POST':
        info_for = Entidadesformulario(request.POST)
        print(info_for)
        if info_for.is_valid():
            info=info_for.cleaned_data
            Entidad= Entidades (tipoentidad=info['tipoentidad'],
                           Documento=info['Documento'], 
                           nombre=info['nombre'])
            Entidad.save()
            return redirect ("Entidades") #pagina a donde lo envio al usuario una vez que guarde los datos
    else: #Metodo get
        info_for=Entidadesformulario()
        return render(request, "Entidadesformulario.html",{"info_for":info_for})


@login_required      
def camionerosformulario (request):
    #Formulario con metodo más manual
    if request.method =='POST':
        datoform= camioneroformulario(request.POST)
        print(datoform)
        if datoform.is_valid():
            dato=datoform.cleaned_data
            camionero=camioneros(Nombre_Completo=dato['Nombre_Completo'],Apellido=dato['Apellido'])
            camionero.save()
            return redirect ("Viajes/")
    else:
        datoform=camioneroformulario()
    return render(request, "formcamionero.html",{"datoform":datoform})

@login_required            
def busquedaviaje (request):
    if request.method == "POST":
        Patente=request.POST["Camion"] 
        Lis_Viajes = Viajes.objects.filter(Q(Camion__icontains=Patente) | Q(Origen__icontains=Patente) | Q(Mercaderia__icontains=Patente)).values() #Para poder filtrar por varias variables
        return render (request, "busquedaviaje.html",{"Viajes":Lis_Viajes})
    else:
        Lis_Viajes = []
        return render (request, "busquedaviaje.html",{"Viajes":Lis_Viajes})
@login_required
def eliminarviaje (request, Viaje_id):
    viaje = Viajes.objects.get(id=Viaje_id)
    viaje.delete()
    return redirect ("consultaviajes")
@login_required
def editarviaje (request,Viaje_id):
    viaje = Viajes.objects.get(id=Viaje_id)
    
    if request.method == 'POST':
        info_formulario = viajesformulario(request.POST)
        print(info_formulario)
        if info_formulario.is_valid():
            infofor=info_formulario.cleaned_data
            viaje.Facturación = infofor["Facturación"]
            viaje.Camion = infofor["Camion"]
            viaje.Origen = infofor["Origen"]
            viaje.Mercaderia = infofor["Mercaderia"]
            viaje.Toneladas = infofor["Toneladas"]
            viaje.Tarifa = infofor["Tarifa"]
            viaje.save()
            return redirect ("consultaviajes")
        
    info_formulario=viajesformulario(initial={"Facturación":viaje.Facturación,
                           "Camion":viaje.Camion, 
                           "Origen":viaje.Origen, 
                           "Mercaderia":viaje.Mercaderia, 
                           "Toneladas":viaje.Toneladas, 
                           "Tarifa":viaje.Tarifa})
    return render(request, "formviajes.html",{"info_formulario":info_formulario})  

class EntidadesList(LoginRequiredMixin, ListView):
    model= Entidades
    template_name= "entidades_list.html"

class EntidadesDetail (LoginRequiredMixin, DetailView):
    model = Entidades
    template_name = "entidad_detail.html"

class EntidadesCreate (LoginRequiredMixin, CreateView):
    model = Entidades
    success_url = "/app_Misviajes/Entidade/list"
    fields= ["tipoentidad", "Documento", "nombre"]

class EntidadesUpdate (LoginRequiredMixin, UpdateView):
    model = Entidades
    success_url= "entidades_form.html"
    fields= ['tipoentidad', 'Documento', 'nombre']

class EntidadesDelete(LoginRequiredMixin, DeleteView):
    model = Entidades
    success_url= "Entidade/list"

    

