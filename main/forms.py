from django import forms
from main.models import Producto

class ProductoForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), required=False, label='Seleccionar Producto')
    class Meta:
        model = Producto
        fields = ['producto','nombre_producto','descri_producto','precio_producto','img_producto','id_categoria']

class ProductoSelectForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label="Seleccionar Producto", required=False)