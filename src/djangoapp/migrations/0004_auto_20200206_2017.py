# Generated by Django 3.0.3 on 2020-02-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_auto_20200206_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Clasificacion',
            field=models.CharField(choices=[('Filtro', 'Filtro'), ('Aceite', 'Aceite'), ('Combustible', 'Combustible'), ('Correa', 'Correa'), ('Rodamientos', 'Rodamientos'), ('Repuestos', 'Repuestos')], default='SELECCIONE', max_length=15),
        ),
    ]
