from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): # Recebe uma request 
    return render(request, 'recipes/pages/home.html')