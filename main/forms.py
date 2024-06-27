from django import forms
from main.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto','descri_producto','precio_producto','img_producto','id_categoria']
