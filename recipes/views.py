from django.shortcuts import render
from django.http import HttpResponse

def sobre(request):
    return render(request, 'recipes/home.html')

def recipe(request, id):
    return render(request, 'recipes/recipe-view.html')