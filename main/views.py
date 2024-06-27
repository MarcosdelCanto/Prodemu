from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProductoForm
from .models import  Producto, Categoria_producto

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

def productosadmin(request, producto_id=None):
    productos = Producto.objects.all()
    if producto_id:
        producto = get_object_or_404(Producto, id=producto_id)
    else:
        producto = None
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto añadido con éxito')
            return redirect('/productos-admin')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'main/productos-admin.html', {
        'form':form,
        'productos':productos
    })

def gestionar_producto(request):
    producto = None
    form_select = ProductoSelectForm(request.POST or None)
    form = ProductoForm()

    if request.method == 'POST':
        if 'seleccionar' in request.POST:
            if form_select.is_valid():
                producto = form_select.cleaned_data['producto']
                if producto:
                    form = ProductoForm(instance=producto)
        else:
            producto = None if form_select.cleaned_data.get('producto') is None else form_select.cleaned_data['producto']
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('productos_list')

    context = {
        'form_select': form_select,
        'form': form,
        'producto': producto
    }

    return render(request, 'productos-admin.html', context)
def productos_categoria(request, id_categoria):
    categoria= get_object_or_404(Categoria_producto, id=id_categoria)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'main/productos.html', {'categoria': categoria,'productos': productos})