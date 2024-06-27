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
    id_categoria = request.GET.get('id_categoria')
    if id_categoria:
        productos = Producto.objects.filter(id_categoria=id_categoria)
    else:
        productos = Producto.objects.all()

    categorias = Categoria_producto.objects.all()
    
    return render(request,'main/productos.html', {
        'productos':productos,
        'categorias':categorias,
        'id_categoria':id_categoria
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
        producto = get_object_or_404(Producto, id_producto=producto_id)
    else:
        producto = None
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto añadido con éxito')
            return redirect('/productos-admin')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'main/productos-admin.html', {
        'form':form,
        'productos':productos,
        'producto_id':producto_id
    })

        

def productos_categoria(request, id_categoria):
    categoria= get_object_or_404(Categoria_producto, id=id_categoria)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'main/productos.html', {'categoria': categoria,'productos': productos})