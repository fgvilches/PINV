from django.db import models
from djangoapp.funciones import *
from multiselectfield import MultiSelectField
from datetime import datetime, date
# Create your models here.
class Producto(models.Model):
    Nombre = models.CharField(max_length=30, blank=True,)
    Codigo_Propio = models.CharField(
        max_length=30,
        blank=True,
    )
    Codigo_de_barras = models.CharField(
        max_length=30,
        blank=True,
    )
    Factura_asociada = models.CharField(
        max_length=30,
        blank=True,
    )
    Maqs = choiceExtractor(readfile("maquinarias","txt"))
    Maquinaria = MultiSelectField(
        choices = Maqs,
        max_choices=100,
        max_length=100,
        blank=True,
    )
    Clasfs = choiceExtractor(readfile("clasificaciones","txt"))
    Clasificacion = models.CharField(
        max_length = 15,
        choices = Clasfs,
        default = "NINGUNA",
    )
    Cantidad_de_producto = models.CharField(max_length=5)
    Cantidad_de_subproducto = models.CharField(
        max_length=5,
        blank=True,
    )
    Locations = choiceExtractor(readfile("ubicaciones","txt"))
    Ubicacion = models.CharField(
        blank=True,
        max_length = 8,
        choices = Locations,
        default = "NINGUNA",
    )
    Sublocations = choiceExtractor(readfile("sububicaciones","txt"))
    SubUbicacion = models.CharField(
        max_length = 7,
        choices = Sublocations,
        default = "NINGUNA",
        blank=True,
    )
    fecha_de_compra = models.DateField("Fecha de Compra(MM/DD/AAAA)",auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    def __str__(self):
        return self.Nombre