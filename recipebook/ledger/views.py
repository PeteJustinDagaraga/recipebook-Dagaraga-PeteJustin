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
    involved_recipe = get_object_or_404(Recipe, pk=num)
    involved_images = RecipeImage.objects.filter(recipe=involved_recipe)
    recipeingredients = RecipeIngredient.objects.filter(recipe=involved_recipe)
    
    return render(request, "recipeEntry.html", {'recipeingredients':recipeingredients, 'recipe': involved_recipe, 'recipeimage': involved_images, 'id': num})

@login_required
def recipeAdd(request):
    if request.method=="POST":

        form_type = request.POST.get('form_type')

        if form_type=="recipe":
            form = RecipeForm(request.POST).save(commit=False)
            form.author = get_object_or_404(Profile, name=request.POST.get('author'))
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

@login_required
def recipeImageAdder(request,num=-1):
    involved_recipe = get_object_or_404(Recipe, pk=num)

    if request.method=="POST":

        form = RecipeImageForm(request.POST, request.FILES).save(commit=False)
        if form.recipe == involved_recipe and form.recipe.author == get_object_or_404(Profile, name=request.POST.get('author')):
            form.save()
            
        return redirect("ledger:recipeEntry", num=num)

    recipeimage_form = RecipeImageForm()

    return render(request, "recipeImageAdder.html", {'recipeimage_form': recipeimage_form, 'recipe': involved_recipe})
