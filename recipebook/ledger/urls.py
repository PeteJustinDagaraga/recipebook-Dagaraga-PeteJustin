from django.urls import path
from .views import recipeList, recipeEntry

urlpatterns = [
    path('recipes/list/', recipeList, name="recipeList"),
    path('recipe/<int:num>/', recipeEntry, name="recipeEntry"),
    ]

app_name = "ledger"
