from django.db import models
from django.contrib.auth.models import User

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto', through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenproducto', blank=True, null=True)

    def __str__(self):
        return f"{self.descripcion} - ${self.precio}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.carrito.usuario.username} - {self.producto.descripcion}"