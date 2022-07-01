from urllib import response

import http
from re import template
from turtle import onclick

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template import Context, Template
from app_Misviajes.models import *

# Create your views here.
def CONSULTAENTIDADES (request):
    Lista_Entidades = Entidades.objects.all()
    ctx= {"Listadoentidades":Lista_Entidades}
    return render (request,"index.html", ctx)

def Viajesrealizadas (request):
    Lista_Viajes = Viajes.objects.all()
    Chofer = "Lautaro Manucci"
    ctx= {"ListaViajes":Lista_Viajes, "Chofer":Chofer}
    return render (request,"viajes.html", ctx) 