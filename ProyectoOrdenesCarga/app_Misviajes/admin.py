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
    def __str__(self):
        return f"{self.nombre}"
    
admin.site.register(Entidades, Entidadesadmin)

class Vehiculaosadmin(admin.ModelAdmin):
    list_display = ("Vehiculo", "Patente", "DescripVeh")
    search_fields= ("Vehiculo", "Patente", "DescripVeh")
    
    def __str__(self):
        return f"{self.Patente}"
    
admin.site.register(Vehiculos, Vehiculaosadmin)

class Localidadadmin(admin.ModelAdmin):
    list_display = ["Nombre", "Provincia", "Codigopost"]
    def __str__(self):
        return f"{self.Nombre} - {self.Provincia}"
    
admin.site.register(Localidades, Localidadadmin)

class Viajesadmin (admin.ModelAdmin):
    list_display = ("Fechacarga", "Fecha", "Cliente", "Tipodoc", "Documento", "Kilometros", "Camion", "Origen", "Destino", "Mercaderia", "Comentario", "Toneladas", "Tarifa", "Documentación", "Facturado", "Fecha_Factura", "Nro_Factura")
    search_fields = ("Fecha","Camion", "Origen", "Mercaderia", "Toneladas", "Tarifa")
    
    def importe (self):
        return round((self.Tarifa * self.Toneladas),2)
    
    def __str__(self):
        return f"Camion: {self.Camion} - Origen:{self.Origen} - Mercaderia:{self.Mercaderia} - Toneladas:{self.Toneladas} Tarifa:{self.Tarifa}"
    
admin.site.register (Viajes, Viajesadmin)

admin.site.register (avatar)

