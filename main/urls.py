from django.urls import path
from .views import inicio, login, carrito, productos, nosotros, userout, productosadmin



urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('carrito/', carrito, name="carrito"),
    path('productos/', productos, name="productos"),
    path('productos-admin/', productosadmin, name='productos-admin'),
    path('nosotros/', nosotros, name="nosotros"),
    path('logout/', userout, name='logout')
]