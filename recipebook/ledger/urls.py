from django.urls import path
from .views import recipeList, recipeEntry, recipeAdd

urlpatterns = [
    path('recipes/list/', recipeList, name="recipeList"),
    path('recipe/<int:num>/', recipeEntry, name="recipeEntry"),
    path('recipe/add/', recipeAdd, name="recipeAdd"),
    ]

app_name = "ledger"
