from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario = FormularioContacto()
    
    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
    
    return render(request, 'Contacto/contacto.html', {
        "miFormulario": formulario
    })