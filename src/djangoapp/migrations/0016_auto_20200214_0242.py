# Generated by Django 3.0.3 on 2020-02-14 05:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0015_auto_20200214_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Maquinaria',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('aaaaaa', 'aaaaaa'), ('aaaasddd', 'aaaasddd')], max_length=100),
        ),
    ]