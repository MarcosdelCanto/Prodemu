from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

def productos(request):
    return render(request,'productos.html')

def nosotros(request):
    return render(request,'sobre_nosotros.html')

def carrito (request):
    return render(request,'carrito.html')