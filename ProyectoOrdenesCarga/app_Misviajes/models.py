from ast import Import
from enum import auto
from operator import length_hint
from pyexpat import model
#from typing_extensions import Self
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class camioneros(models.Model):
    Nombre_Completo=models.CharField (max_length=30)
    Apellido=models.CharField (max_length=30)
    
class Entidades (models.Model):
    Tipos = ((1,"Camioneros"),(2,"Cliente"))
    tipoentidad = models.PositiveSmallIntegerField("Tipo_Entidad", choices=Tipos)
    Documento = models.IntegerField()
    nombre = models.CharField (max_length=30)
    
    def __str__(self):
        return f"{self.nombre}"
        
class Vehiculos (models.Model):
    Tipo_Veh = ((1,"Camion"),(2,"Acoplado"))
    Vehiculo =models.PositiveSmallIntegerField("Tipo_Veh", choices=Tipo_Veh)
    Patente = models.CharField (max_length=7)
    DescripVeh = models.CharField (max_length=30)
    
    def __str__(self):
        return f"{self.Patente}"
    
class Localidades (models.Model):
    Nombre = models.CharField (max_length=30)
    codprov = ((1,"Buenos Aires"),(2,"Cordoba"),(3,"Corrientes"),(4,"Entre Ríos"),(5,"Santa Fe"), (6,"Santiago del Estero"))
    Provincia = models.PositiveSmallIntegerField("Provincia", choices= codprov)
    Codigopost = models.CharField (max_length=4)
    
    def __str__(self):
        return f"{self.Nombre}"

class Viajes (models.Model):
    #Forma_fact=((1,"Toneladas"),(2,"Monto Fijo"))
    #Facturación = models.PositiveSmallIntegerField("Tipo_Fact", choices= Forma_fact) #Para sacar valores de lista
    Fechacarga = models.DateTimeField(auto_now=True)
    Fecha = models.DateField ()
    Cliente = models.ForeignKey(Entidades,null=True, blank=True, on_delete=models.CASCADE)
    tipdoc = ((1,"C.T.G"),(2,"Remito"))
    Tipodoc = models.PositiveSmallIntegerField("Tipo Documento", choices= tipdoc)
    #Camion= models.CharField (max_length=30)
    Documento = models.CharField(max_length=10)
    Listkm= ((1,"50"),(2,"100"),(3,"150"),(4,"200"),(5,"250"),(6,"300"),(7,"350"),(8,"400"),(9,"450"),(10,"500"),(11,"550"),(12,"600"),(13,"650"),(14,"700"),(15,"750"),(16,"800"))
    Kilometros = models.PositiveSmallIntegerField("Km a Recorrer", choices=  Listkm)
    Camion= models.ForeignKey(Vehiculos,null=True, blank=True, on_delete=models.CASCADE) #Para sacar valores de lista
    #Origen=models.CharField (max_length=30)
    Origen= models.ForeignKey(Localidades,null=True, blank=True, on_delete=models.CASCADE) #Para sacar valores de lista 
    Destino = models.ForeignKey(Localidades,null=True, blank=True, on_delete=models.CASCADE,verbose_name="Destino", related_name="ciudaddestino")
    Merc = ((1,"Soja"),(2,"Maiz"),(3,"Trigo"),(4,"Sorgo"),(5,"Girasol"),(6,"Expeller de Soja"),(7,"Afrechillo de Trigo"),(8,"Harina de Soja"),(9,"Otras Mercaderias"))
    Mercaderia = models.PositiveSmallIntegerField("Mercaderia", choices= Merc)
    Comentario= models.CharField(max_length=60, blank=True)
    Toneladas = models.DecimalField(max_digits=5,decimal_places=2)
    Tarifa = models.DecimalField(max_digits=7, decimal_places=2)
    Documentación = models.FileField(upload_to='uploads/%Y/%m/%d/')
    Opcfacturas= ((1,"Si"),(2,"No"))
    Facturado =  models.PositiveSmallIntegerField("Viaje Facturado", choices=  Opcfacturas, default=2)
    Fecha_Factura =  models.DateField (default= '2000-01-01')
    Nro_Factura = models.CharField (max_length=30, default="")
    
    
    def importe (self):
        return round((self.Tarifa * self.Toneladas),2)
    
    
    def __str__(self):
        return f"Camion: {self.Camion} - Origen:{self.Origen} - Mercaderia:{self.Mercaderia} - Toneladas:{self.Toneladas} Tarifa:{self.Tarifa}"
    
class avatar (models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)