# Generated by Django 3.0.3 on 2020-02-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0010_auto_20200210_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Clasificacion',
            field=models.CharField(choices=[('Filtro', 'Filtro'), ('Aceite', 'Aceite'), ('Combustible', 'Combustible'), ('Correa', 'Correa'), ('Rodamientos', 'Rodamientos'), ('Repuestos', 'Repuestos')], default='NINGUNA', max_length=15),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Ubicacion',
            field=models.CharField(choices=[('Bodega 1', 'Bodega 1'), ('Bodega 2', 'Bodega 2')], default='NINGUNA', max_length=8),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_de_compra',
            field=models.DateField(blank=True, null=True),
        ),
    ]
