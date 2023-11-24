from django.shortcuts import render
from .forms import FormularioTesting, FormularioModelo

# Create your views here.
def inicio(request): 
    contexto = {
        'form': FormularioTesting,
        'formModel': FormularioModelo
    }
    return render(request, 'inicio.html', contexto)

def latexEjemplo(request):
    return render(request, 'latexEjemplo.html')