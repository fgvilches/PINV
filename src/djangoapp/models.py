from django.db import models
from funciones import *

# Create your models here.
class Producto(models.Model):
    Nombre = models.CharField(max_length=30)
    Codigo_Propio = models.CharField(max_length=30)
    Codigo_de_barras = models.CharField(max_length=30)
    Factura_asociada = models.CharField(max_length=30)
    Maquinaria = models.CharField(max_length=30)
    Clasfs = choiceExtractor(readfile(cat/clasificaciones,txt))
    Clasificacion = models.CharField(
        max_length = 15,
        choices = Clasfs,
        default = "SELECCIONE",
    )
    Cantidad_de_producto = models.CharField(max_length=5)
    Cantidad_de_subproducto = models.CharField(max_length=5)
    Locations = choiceExtractor(readfile(cat/ubicaciones,txt))
    Ubicacion = models.CharField(
        max_length = 8,
        choices = Locations,
        default = "SELECCIONE",
    )
    Sublocations = choiceExtractor(readfile(cat/sububicaciones,txt))
    SubUbicacion = models.CharField(
        max_length = 7,
        choices = Sublocations,
        default = "NINGUNA",
    )
    def __unicode__(self):
       return self.Nombre