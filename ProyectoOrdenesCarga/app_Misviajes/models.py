from pyexpat import model
from django.db import models

# Create your models here.
class Entidades (models.Model):
    Tipos = ((1,"Camioneros"),(2,"Cliente"))
    tipoentidad = models.PositiveSmallIntegerField("Tipo_Entidad", choices=Tipos)
    Documento = models.IntegerField()
    nombre = models.CharField (max_length=30)
    
class Vehiculos (models.Model):
    Tipo_Veh = ((1,"Camion"),(2,"Acoplado"))
    Vehiculo = models.PositiveSmallIntegerField("Tipo_Veh", choices=Tipo_Veh)
    Patente = models.CharField (max_length=7)
    DescripVeh = models.CharField (max_length=30)
    
class Localidades (models.Model):
    Nombre = models.CharField (max_length=30)

class Viajes (models.Model):
    Forma_Fact =((1,"Toneladas"),(2,"Monto Fijo"))
    Facturación = models.PositiveSmallIntegerField("TipO_Fact", choices= Forma_Fact)
    Camion= models.ForeignKey(Vehiculos,null=True, blank=True, on_delete=models.CASCADE)
    Origen= models.ForeignKey(Localidades,null=True, blank=True, on_delete=models.CASCADE)
    Mercaderia = models.CharField (max_length=30)
    Toneladas = models.IntegerField()
    Tarifa = models.IntegerField()
    