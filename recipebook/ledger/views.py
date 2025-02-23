from django.http import HttpResponse

def recipeList(request):
    return HttpResponse("This is where the RecipeList.html should be")

def recipe1(request):
    return HttpResponse("This is where the Recipe1.html should be")

def recipe2(request):
    return HttpResponse("This is where the Recipe2.html should be")
