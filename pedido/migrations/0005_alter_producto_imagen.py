# Generated by Django 4.1.5 on 2023-06-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos/'),
        ),
    ]
