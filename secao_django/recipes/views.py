from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): # Recebe uma request 
    return render(request, 'recipes/home.html')

def sobre(request): # Recebe uma request 
    return render(request, 'recipes/sobre.html')

def contato(request): # Recebe uma request 
    return render(request, 'recipes/contato.html')