from django.shortcuts import render
from Carrito.models import Producto

# Create your views here.
def home(request):
    return render(request, 'Jaguarete_App/home.html')

def about(request):
    return render(request, 'Jaguarete_App/about.html')

def categoria(request):
    return render(request, 'Jaguarete_App/categoria.html')

def carro(request):
    productos = Producto.objects.all()
    return render(request, 'Jaguarete_App/carrito.html', {
        "productos": productos
    })

# Cambiar views despues de hacer su respectivo login / register
def login(request):
    return render(request, 'Jaguarete_App/login.html')

def register(request):
    return render(request, 'Jaguarete_App/register.html')