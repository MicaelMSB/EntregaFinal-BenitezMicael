from django.shortcuts import render, redirect
from .models import Producto, Carrito, ItemCarrito
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


@login_required
@staff_member_required
def cargar_producto(req):
    if req.method == 'POST':
        form = ProductoForm(req.POST, req.FILES)
        if form.is_valid():
            producto = form.save()
            carrito= Carrito.objects.get(usuario=req.user)
            ItemCarrito.objects.create(carrito=carrito, producto=producto)
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(req, 'cargar_producto.html', {'form': form})

@login_required
@staff_member_required
def actualizar_producto(req, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    if req.method == 'POST':
        form = ProductoForm(req.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(req, 'actualizar_producto.html', {'form': form})

@login_required
@staff_member_required
def eliminar_producto(req, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    producto.delete()
    return redirect('lista_productos')

@login_required
def lista_productos(req):
    productos = Producto.objects.all()
    try:
        carrito = Carrito.objects.get(usuario=req.user)
        total_productos = carrito.productos.count()
    except Carrito.DoesNotExist:
        carrito = None
        total_productos = 0
    return render(req, 'lista_productos.html', {'productos': productos, 'total_productos': total_productos, 'carrito': carrito})

@login_required
def carrito(req):
    carrito = Carrito.objects.get(usuario=req.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    
    if req.method == 'POST':
        for item in items:
            cantidad = req.POST.get('cantidad{}'.format(item.id))
            item.cantidad = cantidad
            item.save()
    
    total = calcular_total_carrito(carrito)
    
    return render(req, 'carrito.html', {'items': items, 'total': total})
@login_required
def agregar_al_carrito(req, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    carrito, created = Carrito.objects.get_or_create(usuario=req.user)
    ItemCarrito.objects.create(carrito=carrito, producto=producto)
    return redirect('lista_productos')

@login_required
def eliminar_del_carrito(req, id_item):
    item = ItemCarrito.objects.get(pk=id_item)
    item.delete()
    return redirect('carrito')

@login_required
def vaciar_carrito(req):
    carrito = Carrito.objects.get(usuario=req.user)
    carrito.productos.clear()
    return redirect('carrito')

def calcular_total_carrito(carrito):
    total = 0
    items = ItemCarrito.objects.filter(carrito=carrito)
    for item in items:
        total += item.producto.precio * item.cantidad
    return total

@login_required
def realizar_compra(request):
    carrito = Carrito.objects.get(usuario=request.user)
    carrito.productos.clear()
    messages.success(request, '¡Gracias por su compra!')
    return redirect('carrito')
