from django import forms
from .models import Producto, Almacen, Ubicacion, MotivoAjuste, Movimiento, Ajuste

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['nombre', 'direccion']

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'descripcion', 'almacen']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categoria', 'cantidad', 'precio','almacen', 'ubicacion']

class MotivoAjusteForm(forms.ModelForm):
    class Meta:
        model = MotivoAjuste
        fields = ['descripcion']

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['producto', 'cantidad', 'tipo', 'origen', 'destino']
    
    tipo = forms.ChoiceField(choices=Movimiento.TIPO_CHOICES, label='Tipo de movimiento')

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        tipo = cleaned_data.get('tipo')

        if cantidad <= 0:
            self.add_error('cantidad', 'La cantidad debe ser mayor que cero.')

        if tipo not in ['Entrada', 'Salida']:
            self.add_error('tipo', 'El tipo de movimiento debe ser "Entrada" o "Salida".')

        return cleaned_data

class AjusteForm(forms.ModelForm):
    class Meta:
        model = Ajuste
        fields = ['producto', 'motivo','almacen', 'ubicacion', 'movimiento']

class AsignarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['ubicacion', 'nombre']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['readonly'] = True 
