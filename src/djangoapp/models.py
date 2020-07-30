from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime, date
# Create your models here.

#Se define clase clasificaciones para poder actualizarlas sin uso de archivos externos
class Clasificaciones(models.Model):
    Clasificacion = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.Clasificacion
#Samee
class Maquinarias(models.Model):
    Maquinaria = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.Maquinaria
#Samee
class Ubicaciones(models.Model):
    Ubicacion = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.Ubicacion
#Samee
class SubUbicaciones(models.Model):
    SubUbicacion = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.SubUbicacion

#Se dfine clase producto para mejor estructura
class Producto(models.Model):
    Nombre = models.CharField(max_length=50, blank=True)
    Codigo_Propio = models.CharField(max_length=50, blank=True)
    Codigo_de_barras = models.CharField(max_length=50, blank=True)
    Factura_asociada = models.CharField(max_length=50, blank=True)
    #Ciclo para extraer maquinarias actualizadas (se hizo de este modo para facilitar la seleccion)
    Maquinaria = MultiSelectField(
        choices = [(instance.id, str(instance)) for instance in Maquinarias.objects.all()],
        max_choices=100,
        max_length=100,
        blank=True,
    )
    Clasificacion = models.ForeignKey(Clasificaciones, blank=True, null=True, on_delete=models.CASCADE)
    Cantidad_de_producto = models.CharField(max_length=5)
    Cantidad_de_subproducto = models.CharField(max_length=5, blank=True)
    Ubicacion = models.ForeignKey(Ubicaciones, blank=True, null=True, on_delete=models.CASCADE)
    SubUbicacion = models.ForeignKey(SubUbicaciones, blank=True, null=True, on_delete=models.CASCADE)
    fecha_de_compra = models.DateField("Fecha de Compra(MM/DD/AAAA)",auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    exportar = models.BooleanField(default=False)
    def __str__(self):
        return self.Nombre
