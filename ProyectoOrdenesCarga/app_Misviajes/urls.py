from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views import *
#from django.conf import settings
#from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views import *
#from django import views

from app_Misviajes.views import *

urlpatterns = [
    path('', INICIO, name="inicio"),
    path('base/', base, name="base"),
    path('acercade', acercade, name="acercade"),
    #path('Viajes/', Viajesrealizadas,name="Viajes"),
    path('Entidades/', CONSULTAENTIDADES, name="Entidades"),
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('eliminarentidad/<Entidad_id>', eliminarentidad, name="eliminarentidad"),
    path('editarentidad/<Entidad_id>', editarentidad, name="editarentidad"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('Vehiculosformulario', vehiculosformularios, name="Vehiculosformulario"),
    path('editarvehiculo/<Vehiculo_id>', vehiculoseditar, name="editarvehiculo"),
    path('eliminarvehiculo/<Vehiculo_id>', eliminarvehiculo, name="eliminarvehiculo"),
    # otra forma de ver las entidades y sus opciones
    path('Entidade/list/', EntidadesList.as_view(), name='Entidades_list'),
    path('Entidade/<pk>', EntidadesDetail.as_view(), name='detail'),
    path('Entidade/nuevo', EntidadesCreate.as_view(), name='Entidade_create'),
    path('Entidade/editar/<pk>', EntidadesUpdate.as_view(), name='Entidade_update'),
    path('Entidade/eliminar/<pk>', EntidadesDelete.as_view(), name='Entidade_Delete'),
    path('Entidade/list/', EntidadesList.as_view(), name='Entidades_list'),
    #Metodo original que dimos en el curso
    #path(r'^(?P<pk>\d+)$', EntidadesDetail.as_view(), name='detail'),
    #path(r'^nuevo$', EntidadesCreate.as_view(), name='Entidade_create'),
    #path(r'^editar/(?P<pk>\d+)$', EntidadesUpdate.as_view(), name='Entidade_update'),
    #path(r'^eliminar/(?P<pk>\d+)$', EntidadesDelete.as_view(), name='Entidade_Delete'),
    
    path('Viajesformulario', Viajesformulario, name="FormularioViajes"),
    path('Entidades/Entidadesformulario', Entidadesformularios, name="FormularioViajes"),
    path('entidades/camioneros', camionerosformulario),
    path('consultaviajes', busquedaviaje, name="consultaviajes"),
    path('eliminarviaje/<Viaje_id>', eliminarviaje, name="eliminarviaje"),
    path('editarviaje/<Viaje_id>', editarviaje, name="editarviaje"),
    path('facturarviaje/<Viaje_id>', facturacion, name="facturarviaje")
    ,] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)