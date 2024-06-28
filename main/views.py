from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ProductoForm
from .models import  Producto, Categoria_producto, Carro_compra, Detalle_carro
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def inicio(request):
    return render(request, 'main/inicio.html')

def login(request):
    return render(request, 'main/login.html')

def nosotros(request):
    return render(request,'main/sobre_nosotros.html')

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    carrito, created = Carro_compra.objects.get_or_create(usuario=request.user)

    item_carrito, created = Detalle_carro.objects.get_or_create(id_carro=carrito, id_producto=producto)
    if not created:
        item_carrito.cantidad_prod += 1
        item_carrito.save()

    return redirect('/productos')

@login_required
def ver_carrito(request):
    carrito, created = Carro_compra.objects.get_or_create(usuario=request.user)
    
    items_carrito = Detalle_carro.objects.filter(id_carro=carrito)
    items_carrito_w = items_carrito.values(
        'id_producto__nombre_producto',
        'id_producto__precio_producto',
        'cantidad_prod',
    )
    items_carrito_list = list(items_carrito_w)
    items_carrito_json = json.dumps(items_carrito_list, cls=DjangoJSONEncoder)
    
    return render(request, 'main/ver_carrito.html', 
        {'items_carrito': items_carrito,
        'items_carrito_json': items_carrito_json,
        'carrito':carrito
    })
    
# @login_required
# def limpiar_carrito(request):
#     if request.method == 'POST':
#         carrito_id = request.POST.get('carrito_id')
#         if carrito_id:
#             carrito = Carro_compra.objects.get(id_carro=int(carrito_id))
#             carrito.detalle_carro.all().delete()
#             carrito.delete()
#             return redirect('/productos')
#     # Manejar el caso donde no se puede limpiar el carrito
#     return render(request, 'main/ver_carrito.html', {'mensaje': 'No se pudo limpiar el carrito.'})

@login_required
def limpiar_carrito(request):
    if request.method == 'POST':
        carrito_id = request.POST.get('carrito_id')
        print(f"carrito_id: {carrito_id}")  # Depuración: Imprimir el carrito_id recibido
        
        if carrito_id and carrito_id.strip():
            try:
                carrito = get_object_or_404(Carro_compra, id_carro=int(carrito_id))
                
                print(f"Carrito encontrado: {carrito}")  # Depuración: Imprimir el carrito encontrado
                
                Detalle_carro.objects.filter(id_carro=carrito).delete()
                carrito.delete()
                print("Carrito limpiado y eliminado de la base de datos.")  # Depuración: Confirmación de eliminación
                
                return redirect('/productos')
            except Carro_compra.DoesNotExist:
                print("El carrito no existe.")  # Depuración: Carrito no encontrado
                return render(request, 'main/ver_carrito.html', {'mensaje': 'El carrito no existe.'})
            except ValueError:
                print("ID de carrito inválido.")  # Depuración: ID de carrito inválido
                return render(request, 'main/ver_carrito.html', {'mensaje': 'ID de carrito inválido.'})
    # Manejar el caso donde no se puede limpiar el carrito
    print("No se pudo limpiar el carrito.")  # Depuración: Caso de error general
    return render(request, 'main/ver_carrito.html', {'mensaje': 'No se pudo limpiar el carrito.'})


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