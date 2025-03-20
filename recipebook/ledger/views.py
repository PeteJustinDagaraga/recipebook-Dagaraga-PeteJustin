from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required

@login_required
def recipeList(request):
    recipes = Recipe.objects.all()
    return render(request, "recipeList.html", {'recipes':recipes})

@login_required
def recipeEntry(request,num=-1):
    if num in range(1,3):
        recipeingredients = RecipeIngredient.objects.filter(recipe__name="Recipe "+str(num))
    else:
        return HttpResponse(loader.get_template("404.html").render())
    return render(request, "recipeEntry.html", {'recipeingredients':recipeingredients})
