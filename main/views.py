from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProductoForm
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

def productos(request):
    productos = Producto.objects.all()
    return render(request,'main/productos.html', {
        'productos':productos
    })

def userout(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('/')

@login_required
@permission_required('main.add_producto')
def productosadmin(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto añadido con éxito')
    else:
        form = ProductoForm()
    return render(request, 'main/productos-admin.html', {
        'form':form,
        'productos':productos
    })