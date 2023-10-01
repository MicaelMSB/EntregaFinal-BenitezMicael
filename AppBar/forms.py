from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class AvatarFormulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=('imagen',)

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Ingrese nombre de usuario")
    first_name = forms.CharField(label="Ingrese su nombre")
    last_name = forms.CharField(label="Ingrese su apellido")
    email = forms.EmailField(label="Ingrese email")
    age = forms.IntegerField(label="Ingrese su edad")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'age']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
            'age': 'Edad',
        }

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):

        print(self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2   
         
class FormContacto(forms.Form):
    subject = forms.CharField(max_length=200, label="Asunto")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return message         