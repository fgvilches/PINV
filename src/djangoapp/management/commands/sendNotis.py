# Python Code
# myapp/management/commands/mytask.py
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from djangoapp.models import Producto
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'No hay ayuda para ti jeje'

    def handle(self, *args, **options):
        queryset0 = Producto.objects.all().order_by('-timestamp').filter(Cantidad_de_producto__iexact=0)
        queryset1 = Producto.objects.all().order_by('-timestamp').filter(Cantidad_de_producto__iexact=1)
        cant_sinEx = 0
        usuarios = []
        users = User.objects.all().order_by('-id')
        for user in users:
            mail = str(user.email)
            usuarios.append(mail)
        for object in queryset0:
            cant_sinEx += 1
        cant_pProntos = 0
        for object in queryset1:
            cant_pProntos += 1
        saludo_mail = 'Hola, \n Este es un mensaje automatizado de PINV Software \n'
        separador = '================================================== \n'
        mensaje = saludo_mail + separador +  str(cant_sinEx) +  ' productos sin existencia en el inventario. \n'
        for producto in queryset0:
            nombre = " ● " + str(producto.Nombre) + ". \n"
            mensaje += nombre
        mensaje += separador + str(cant_pProntos) + ' productos prontos a acabarse. \n'
        for producto in queryset1:
            nombre = " ● " + str(producto.Nombre) + ".\n"
            mensaje += nombre
        mensaje += separador + "Para ver el detalle ve al panel del software."
        for usuario in usuarios:
            send_mail(
                'PINV Software - Reporte Semanal',
                mensaje,
                'pinv.software@gmail.com',
                [usuario],
                fail_silently=False,
            )
        self.stdout.write('==================================')
        self.stdout.write('Notificaciones semanales enviadas!')
        self.stdout.write('==================================')