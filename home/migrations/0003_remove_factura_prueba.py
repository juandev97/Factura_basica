# Generated by Django 3.1.3 on 2020-11-04 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_factura_prueba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='prueba',
        ),
    ]
