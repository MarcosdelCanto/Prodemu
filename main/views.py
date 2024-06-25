from django.shortcuts import render
from django.contrib.auth import logout
from .models import Cliente, Pago, Orden, Categoria_producto, Producto, Detalle_carro, Carro_compra

# Create your views here.
def inicio(request):
    return render(request, 'main/inicio.html')

def login(request):
    return render(request, 'main/login.html')

def nosotros(request):
    return render(request,'main/sobre_nosotros.html')

def carrito (request):
    return render(request,'main/carrito.html')

#CRUD PRODUCTOS

def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos':productos
    }
    return render(request,'main/productos.html', context)

def userout(request):
    logout(request)
    return render(request, 'main/inicio.html')