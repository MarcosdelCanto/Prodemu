from django.urls import path, include
from .views import inicio, login, carrito, productos, nosotros, userout



urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('carrito/', carrito, name="carrito"),
    path('productos/', productos, name="productos"),
    path('nosotros/', nosotros, name="nosotros"),
    path('logout/', userout, name='logout')
]