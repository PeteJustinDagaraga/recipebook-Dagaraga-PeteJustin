from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required

@login_required
def recipeList(request):
    recipes = Recipe.objects.all()
    return render(request, "recipeList.html", {'recipes':recipes})

@login_required
def recipeEntry(request,num=-1):
    input_recipe_name = "Recipe "+str(num)
    involved_recipe = get_object_or_404(Recipe, name=input_recipe_name)
    recipeingredients = RecipeIngredient.objects.filter(recipe=involved_recipe)
    print(recipeingredients)
    
    return render(request, "recipeEntry.html", {'recipeingredients':recipeingredients, 'recipe': involved_recipe})
