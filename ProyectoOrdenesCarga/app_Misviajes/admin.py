from django.contrib import admin

from app_Misviajes.models import *

#Register your models here.
class Entidadesadmin(admin.ModelAdmin):
    list_display = ("tipoentidad", "Documento", "nombre")
    list_display = ("tipoentidad", "Documento", "nombre")
admin.site.register(Entidades, Entidadesadmin)

class Vehiculaosadmin(admin.ModelAdmin):
    list_display = ("Vehiculo", "Patente", "DescripVeh")
admin.site.register(Vehiculos, Vehiculaosadmin)

class Localidadadmin(admin.ModelAdmin):
    list_display = ["Nombre"]
admin.site.register(Localidades, Localidadadmin)

class Viajesadmin (admin.ModelAdmin):
    list_display = ("Facturación", "Camion", "Origen", "Mercaderia", "Toneladas", "Tarifa")
admin.site.register (Viajes, Viajesadmin)

