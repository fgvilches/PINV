# Generated by Django 3.0.3 on 2020-02-14 05:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0014_auto_20200214_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Maquinaria',
        ),
        migrations.AddField(
            model_name='producto',
            name='Maquinaria',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('G145J', 'G145J'), ('G145J', 'G145J'), ('G145J', 'G145J'), ('G145J', 'G145J'), ('G145J', 'G145J'), ('G145J', 'G145J'), ('G145J', 'G145J')], max_length=100),
        ),
    ]
