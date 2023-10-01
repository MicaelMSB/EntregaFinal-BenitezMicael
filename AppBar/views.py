
from django.shortcuts import render, redirect
from .models import Avatar, MensajeContacto
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AvatarFormulario, UserEditForm, RegistrationForm, FormContacto
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import get_resolver


def inicio(req):
    if req.user.is_authenticated:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    else:
        return render(req, "inicio.html")
    
def loginView(req):

    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            password = data["password"]

            user = authenticate(username=usuario, password=password)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido a SanviShop {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": f"Los datos ingresados son incorrectos"})
        else: 
            return render(req, "inicio.html", {"mensaje": f"El formulario es invalido"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
def register(req):
    if req.method == 'POST':
        registration_form = RegistrationForm(req.POST)
        avatar_form = AvatarFormulario(req.POST, req.FILES)
        if registration_form.is_valid() and avatar_form.is_valid():
            user = registration_form.save()
            avatar = avatar_form.cleaned_data['imagen']
            Avatar.objects.create(user=user, imagen=avatar)
            return render(req, 'inicio.html', {"mensaje": f"Usuario creado con éxito"})
    else:
        registration_form = RegistrationForm()
        avatar_form = AvatarFormulario()
    return render(req, 'registro.html', {'registration_form': registration_form, 'avatar_form': avatar_form})
    
@login_required    
def editar_perfil(req):
    usuario = req.user
    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado con éxito"})
        else:
            return render(req, "editar_perfil.html", {"miFomulario": miFormulario})
    else:
        miFormulario = UserEditForm(instance=req.user)
        return render(req, "editar_perfil.html", {"miFomulario": miFormulario})
    
@login_required  
def agregar_avatar(req):
    if req.method == 'POST':
        miFormulario = AvatarFormulario(req.POST, req.FILES)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            try:
                avatar_anterior = Avatar.objects.get(user=req.user)
                avatar_anterior.imagen.delete()
                avatar_anterior.delete()
            except Avatar.DoesNotExist:
                pass
            avatar_nuevo = Avatar(user=req.user, imagen=data["imagen"])
            avatar_nuevo.save()
            return render(req, "inicio.html", {"mensaje": "Avatar actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario Inválido"})
    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})
    
def acercademi(req):
    return render(req, 'acercademi.html')    

def lista_urls(req):
    url_resolver = get_resolver(None)
    url_patterns = url_resolver.reverse_dict.keys()
    return render(req, 'list_urls.html', {'url_patterns': url_patterns})

@login_required
def contacto(request):
    if request.method == 'POST':
        form = FormContacto(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            user = request.user
            MensajeContacto.objects.create(user=user, subject=subject, message=message)
            return redirect('contacto_exitoso')
    else:
        form = FormContacto()
    return render(request, 'contacto.html', {'form': form})

@login_required
def contacto_exitoso(request):
    return render(request, 'contacto_exitoso.html')

