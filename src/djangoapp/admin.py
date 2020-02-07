from django.contrib import admin

# Register your models here.
from .models import Producto

from .forms import ProductoForm


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["Nombre", "Codigo_Propio","Clasificacion"]
    form = ProductoForm
    list_filter = ['Nombre', 'Codigo_Propio']
    search_fields = ['Nombre', 'Codigo_Propio']

admin.site.register(Producto, ProductoAdmin)