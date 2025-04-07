from django.urls import path
from .views import recipeList, recipeEntry, recipeAdd, recipeImageAdder

urlpatterns = [
    path('recipes/list/', recipeList, name="recipeList"),
    path('recipe/<int:num>/', recipeEntry, name="recipeEntry"),
    path('recipe/add/', recipeAdd, name="recipeAdd"),
    path('recipe/<int:num>/add_image', recipeImageAdder, name="recipeImageAdder"),
    ]

app_name = "ledger"
