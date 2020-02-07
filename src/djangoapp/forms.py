from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Nombre', 'Codigo_Propio', 'Codigo_de_barras', 'Factura_asociada', 'Maquinaria','Clasificacion','Cantidad_de_producto','Cantidad_de_subproducto','Ubicacion','SubUbicacion']
