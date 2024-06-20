from django.urls import path
from .views import inicio, login, carrito, productos, nosotros



urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('carrito/', carrito, name="carrito"),
    path('productos/', productos, name="productos"),
    path('nosotros/', nosotros, name="nosotros"),
]