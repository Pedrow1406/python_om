from django.shortcuts import render
from django.http import HttpResponse
from .util.recipes.factory import make_recipe
# Create your views here.
def home(request): # Recebe uma request 
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(20)]
    })

def recipes(request, id): # Recebe uma request 
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe':make_recipe,
        'is_detail_page': True
    })
