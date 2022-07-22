from django.contrib import admin
from django.urls import path
from django.views import *

from django.contrib import admin
from django.urls import path
from django.views import *
from django import views

from app_Misviajes.views import *

urlpatterns = [
    path('', INICIO, name="inicio"),
    path('Viajes/', Viajesrealizadas,name="Viajes"),
    path('Entidades/', CONSULTAENTIDADES, name="Entidades"),
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    
    path('Entidade/list/', EntidadesList.as_view(), name='Entidades_list'),
    path(r'^(?P<pk>\d+)$', EntidadesDetail.as_view(), name='detail'),
    path(r'^nuevo$', EntidadesCreate.as_view(), name='Entidade_create'),
    path(r'^editar/(?P<pk>\d+)$', EntidadesUpdate.as_view(), name='Entidade_update'),
    path(r'^eliminar/(?P<pk>\d+)$', EntidadesDelete.as_view(), name='Entidade_Delete'),
    
    path('Viajesformulario', Viajesformulario, name="FormularioViajes"),
    path('Entidades/Entidadesformulario', Entidadesformularios, name="FormularioViajes"),
    path('entidades/camioneros', camionerosformulario),
    path('consultaviajes', busquedaviaje, name="consultaviajes"),
    path('eliminarviaje/<Viaje_id>', eliminarviaje, name="eliminarviaje"),
    path('editarviaje/<Viaje_id>', editarviaje, name="editarviaje")
    ,]