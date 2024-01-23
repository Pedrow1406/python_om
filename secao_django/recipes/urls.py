from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='recipe-home'), # Home
    path('recipes/<int:id>/', views.recipes, name='recipe-recipes'), # recipes
]
