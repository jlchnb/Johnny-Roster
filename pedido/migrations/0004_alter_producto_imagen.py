# Generated by Django 4.1.5 on 2023-06-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_rename_tipo_comida_producto_id_tipocomida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos/media'),
        ),
    ]
