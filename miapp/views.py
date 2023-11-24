from django.shortcuts import render
from .forms import FormularioTesting

# Create your views here.
def inicio(request): 
    contexto = {
        'form': FormularioTesting
    }
    return render(request, 'inicio.html', contexto)