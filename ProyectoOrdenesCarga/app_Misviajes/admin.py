from django.contrib import admin

from app_Misviajes.models import *

#Register your models here.
class camionerosadmin(admin.ModelAdmin):
    list_display= ("Nombre_Completo", "Apellido")
    search_fields = ("Nombre_Completo", "Apellido")
admin.site.register(camioneros, camionerosadmin)

class Entidadesadmin(admin.ModelAdmin):
    list_display = ("tipoentidad", "Documento", "nombre")
    search_fields =("tipoentidad", "Documento", "nombre")
admin.site.register(Entidades, Entidadesadmin)

class Vehiculaosadmin(admin.ModelAdmin):
    list_display = ("Vehiculo", "Patente", "DescripVeh")
    search_fields= ("Vehiculo", "Patente", "DescripVeh")
admin.site.register(Vehiculos, Vehiculaosadmin)

class Localidadadmin(admin.ModelAdmin):
    list_display = ["Nombre"]
admin.site.register(Localidades, Localidadadmin)

class Viajesadmin (admin.ModelAdmin):
    list_display = ("Facturación", "Camion", "Origen", "Mercaderia", "Toneladas", "Tarifa")
    search_fields = ("Facturación","Camion", "Origen", "Mercaderia", "Toneladas", "Tarifa")
    def __str__(self):
        return f"Facturación: {self.Facturación} - Camion: {self.Camion} - Origen:{self.Origen} - Mercaderia:{self.Mercaderia} - Toneladas:{self.Toneladas} Tarifa:{self.Tarifa}"
admin.site.register (Viajes, Viajesadmin)



