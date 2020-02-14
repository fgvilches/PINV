from django.contrib import admin

# Register your models here.
from .models import Producto, Clasificaciones, Maquinarias, Ubicaciones, SubUbicaciones

from .forms import ProductoForm


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["Nombre", "Codigo_Propio","Clasificacion","fecha_de_compra","timestamp"]
    form = ProductoForm
    list_filter = ['Nombre', 'Codigo_Propio']
    search_fields = ['Nombre', 'Codigo_Propio']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Clasificaciones)
admin.site.register(Maquinarias)
admin.site.register(Ubicaciones)
admin.site.register(SubUbicaciones)