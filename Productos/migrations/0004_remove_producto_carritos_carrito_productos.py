# Generated by Django 4.2.4 on 2023-09-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_carrito_alter_producto_imagen_itemcarrito_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='carritos',
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='Productos.ItemCarrito', to='Productos.producto'),
        ),
    ]
