from django.shortcuts import render, redirect
from .forms import ProductoForm, ProductoSearchForm
from .models import Producto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv
# Create your views here.
def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "home.html",context)
def add(request):
    title = 'Añadir Productos'
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/inventario')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "add.html",context)

def inventario(request):
    title = 'Inventario'
    queryset = Producto.objects.all()
    form = ProductoSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form" : form,
    }
    if request.method == 'POST':
        queryset = Producto.objects.all().order_by('-timestamp').filter(
            Nombre__icontains=form['Nombre'].value(),
            Codigo_de_barras__icontains=form['Codigo_de_barras'].value(),
            Ubicacion__icontains=form['Ubicacion'].value(),
            Factura_asociada__icontains=form['Factura_asociada'].value()
        )
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
        if form['exportar'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Busqueda inventario.csv"'
            writer = csv.writer(response)
            writer.writerow(['Nombre', 'Codigo de barras', 'Ubicacion', 'Factura_asociada','Cantidad'])
            instance = queryset
            for row in instance:
                writer.writerow([row.Nombre, row.Codigo_de_barras, row.Ubicacion, row.Factura_asociada, row.Cantidad_de_producto])
            return response
    return render(request, "inventario.html", context)

def edit(request, id=None):
    instance = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/inventario')
    context = {
            "title": 'Editar ' + str(instance.Nombre),
            "instance": instance,
            "form": form,
        }
    return render(request, "add.html", context)


def delete(request, id=None):
    instance = get_object_or_404(Producto, id=id)
    instance.delete()
    return redirect("inventario")