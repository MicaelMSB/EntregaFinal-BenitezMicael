from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'precio', 'stock', 'imagen'] 
        labels = {
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'stock': 'Stock',
            'imagen': 'Imagen',  
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        