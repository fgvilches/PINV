from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Nombre', 'Codigo_Propio', 'Codigo_de_barras', 'Factura_asociada', 'Maquinaria','Clasificacion','Cantidad_de_producto','Cantidad_de_subproducto','Ubicacion','SubUbicacion', 'fecha_de_compra']

    def clean_Nombre(self):
        name = self.cleaned_data.get('Nombre')
        if (name == ""):
            raise forms.ValidationError('Este campo no se puede dejar en blanco.')
        return name

    def clean_Codigo_Propio(self):
        codigo = self.cleaned_data.get('Codigo_Propio')
        if (codigo == ""):
            raise forms.ValidationError('Este campo no se puede dejar en blanco.\n Recuerda que puedes generarlo.')
        for instance in Producto.objects.all():
            if instance.Codigo_Propio == codigo:
                raise forms.ValidationError('Ya existe un producto con el codigo ' + codigo)
        return codigo


    def clean_Codigo_de_barras(self):
        codigo = self.cleaned_data.get('Codigo_de_barras')
        if (codigo == ""):
            raise forms.ValidationError('Este campo no se puede dejar en blanco.\n Recuerda que puedes generarlo.')
        for instance in Producto.objects.all():
            if instance.Codigo_de_barras == codigo:
                raise forms.ValidationError('El producto codigo '+ codigo +' ya está registrado bajo el nombre ' + instance.Nombre)
        return codigo


class ProductoSearchForm(forms.ModelForm):
    class Meta:
        model = Producto
        #add ubicacion
        fields = ['Nombre', 'Codigo_de_barras','Factura_asociada', 'exportar']