# Generated by Django 4.2.2 on 2023-06-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_remove_orden_cantidad_remove_orden_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo_comida',
            field=models.CharField(choices=[('broaster', 'Broaster'), ('carne', '100% carne'), ('vegetariana', 'Vegetariana'), ('acompanamiento', 'Acompañamiento')], max_length=20),
        ),
    ]