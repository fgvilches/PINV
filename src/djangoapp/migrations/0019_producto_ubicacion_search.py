# Generated by Django 3.0.3 on 2020-02-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0018_producto_exportar'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Ubicacion_search',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]