from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/ ', loginView, name="login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),

]



