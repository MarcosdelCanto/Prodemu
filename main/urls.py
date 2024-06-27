from django.urls import path
from .views import inicio, login, ver_carrito, productos, nosotros, userout, productosadmin, agregar_al_carrito



urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name="carro"),
    path('productos/', productos, name="productos"),
    path('productos-admin/', productosadmin, name='crear_producto'),
    path('productos-admin/<int:producto_id>/', productosadmin, name='editar_producto'),
    path('nosotros/', nosotros, name="nosotros"),
    path('logout/', userout, name='logout')
]