from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import loader
from .models import Recipe, RecipeIngredient, RecipeImage, Profile
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm

@login_required
def recipeList(request):
    recipes = Recipe.objects.all()
    return render(request, "recipeList.html", {'recipes':recipes})

@login_required
def recipeEntry(request,num=-1):
    input_recipe_name = "Recipe "+str(num)
    involved_recipe = get_object_or_404(Recipe, name=input_recipe_name)
    involved_images = RecipeImage.objects.filter(recipe=involved_recipe)
    recipeingredients = RecipeIngredient.objects.filter(recipe=involved_recipe)
    print(recipeingredients)
    
    return render(request, "recipeEntry.html", {'recipeingredients':recipeingredients, 'recipe': involved_recipe, 'recipeimage': involved_images})

@login_required
def recipeAdd(request):
    if request.method=="POST":

        form_type = request.POST.get('form_type')

        if form_type=="recipe":
            form = RecipeForm(request.POST).save(commit=False)
            print(request.POST.get('author'))
            form.author = get_object_or_404(Profile, name=request.POST.get('author'))
            print(form.author.bio)
            form.save()

        elif form_type=="ingredient":
            form = IngredientForm(request.POST)
            if form.is_valid():
                form.save()

        elif form_type=="recipeingredient":
            form = RecipeIngredientForm(request.POST).save(commit=False)
            author = get_object_or_404(Profile, name=request.POST.get('author'))

            if form.recipe.author == author:
                form.save()

        return redirect("ledger:recipeAdd")

    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipeingredient_form = RecipeIngredientForm()

    return render(request, "recipeAdd.html", {'recipe_form': recipe_form, 'ingredient_form': ingredient_form, 'recipeingredient_form': recipeingredient_form})
