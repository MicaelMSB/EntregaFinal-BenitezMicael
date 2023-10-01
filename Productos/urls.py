from django.urls import include, path
from . import views
from .views import *


urlpatterns = [
    path('cargar_producto/', views.cargar_producto, name='cargar_producto'),
    path('actualizar_producto/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('', views.lista_productos, name='lista_productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:id_producto>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:id_item>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('realizar_compra/', views.realizar_compra, name='realizar_compra'),
]