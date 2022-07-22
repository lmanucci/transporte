from pyexpat import model
from django.db import models

# Create your models here.
class camioneros(models.Model):
    Nombre_Completo=models.CharField (max_length=30)
    Apellido=models.CharField (max_length=30)
    
class Entidades (models.Model):
    Tipos = ((1,"Camioneros"),(2,"Cliente"))
    tipoentidad = models.PositiveSmallIntegerField("Tipo_Entidad", choices=Tipos)
    Documento = models.IntegerField()
    nombre = models.CharField (max_length=30)
        
class Vehiculos (models.Model):
    Tipo_Veh = ((1,"Camion"),(2,"Acoplado"))
    Vehiculo =models.PositiveSmallIntegerField("Tipo_Veh", choices=Tipo_Veh)
    Patente = models.CharField (max_length=7)
    DescripVeh = models.CharField (max_length=30)
    
class Localidades (models.Model):
    Nombre = models.CharField (max_length=30)

class Viajes (models.Model):
    #Forma_fact=((1,"Toneladas"),(2,"Monto Fijo"))
    #Facturación = models.PositiveSmallIntegerField("Tipo_Fact", choices= Forma_fact) #Para sacar valores de lista
    Facturación = models.CharField (max_length=30)
    Camion= models.CharField (max_length=30)
    #Camion= models.ForeignKey(Vehiculos,null=True, blank=True, on_delete=models.CASCADE) #Para sacar valores de lista
    Origen=models.CharField (max_length=30)
    #Origen= models.ForeignKey(Localidades,null=True, blank=True, on_delete=models.CASCADE) #Para sacar valores de lista
    Mercaderia = models.CharField (max_length=30)
    Toneladas = models.IntegerField()
    Tarifa = models.IntegerField()
    
    
    def __str__(self):
        return f"Facturación: {self.Facturación} - Camion: {self.Camion} - Origen:{self.Origen} - Mercaderia:{self.Mercaderia} - Toneladas:{self.Toneladas} Tarifa:{self.Tarifa}"