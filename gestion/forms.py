from django import forms
from .models import Cliente, Transaccion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['tipo', 'monto', 'descripcion']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 10000'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Depósito o compra'}),
        }