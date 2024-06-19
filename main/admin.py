from django.contrib import admin
from .models import Cliente, Pago, Orden, Categoria_producto, Producto, Detalle_carro, Carro_compra
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Orden)
admin.site.register(Categoria_producto)
admin.site.register(Producto)
admin.site.register(Detalle_carro)
admin.site.register(Carro_compra)