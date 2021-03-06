from django.shortcuts import render, redirect
from .forms import ProductoForm, ProductoSearchForm
from .models import Producto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import csv
# Create your views here.
def home(request):
    title = 'Bienvenido a PINV Software - Transportes Araya'
    context = {
        "title": title,
    }
    return render(request, "home.html",context)
def add(request):
    title = 'Añadir Productos'
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto creado exitosamente!')
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
        "form": form,
    }
    if request.method == 'POST':
        queryset = Producto.objects.all().order_by('-timestamp').filter(Nombre__icontains=form['Nombre'].value(), Codigo_de_barras__icontains=form['Codigo_de_barras'].value(), Codigo_Propio__icontains=form['Codigo_Propio'].value(), Factura_asociada__icontains=form['Factura_asociada'].value())
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
        if form['exportar'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Busqueda_inventario.xls"'
            writer = csv.writer(response)
            writer.writerow(['Nombre', 'Codigo de barras', 'Faactura_asociada','Cantidad'])
            instance = queryset
            for row in instance:
                writer.writerow([row.Nombre, row.Codigo_de_barras, row.Factura_asociada, row.Cantidad_de_producto])
            return response

    return render(request, "inventario.html", context)

def edit(request, id=None):
    instance = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Edicion Exitosa!')
        return redirect('/inventario')
    context = {
            "title": 'Editar ' + str(instance.Nombre),
            "instance": instance,
            "form": form,
        }
    return render(request, "edit.html", context)


def delete(request, id=None):
    instance = get_object_or_404(Producto, id=id)
    instance.delete()
    return redirect("inventario")

def panel(request,):
    title = 'Panel de Notificaciones'
    queryset0 = Producto.objects.all().order_by('-timestamp').filter(Cantidad_de_producto__iexact=0)
    queryset1 = Producto.objects.all().order_by('-timestamp').filter(Cantidad_de_producto__iexact=1)
    queryset2 = Producto.objects.all().order_by('-timestamp').filter(Cantidad_de_producto__iexact=2)
    p_sinExistencia = queryset0
    p_Prontos = queryset1
    cant_sinEx = 0
    for object in p_sinExistencia:
        cant_sinEx += 1
    cant_pProntos = 0
    for object in p_Prontos:
        cant_pProntos += 1
    stock = 'Stock Crítico'
    alertas = 'Alertas'
    context = {
        "title": title,
        "stock": stock,
        "cant_sinEx": cant_sinEx,
        "p_sinExistencia": p_sinExistencia,
        "cant_pProntos": cant_pProntos,
        "p_Prontos": p_Prontos,
        "alertas": alertas,
        "queryset0": queryset0,
        "queryset1": queryset1,
        "queryset2": queryset2,
    }
    return render(request, "panel.html",context)



