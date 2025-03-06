from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = None
    list_editable = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = None
    list_editable = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('quantity','ingredient__name',)
    list_filter = ('recipe__name',)
    search_fields = ['ingredient__name','recipe__name']
    list_display_links = None
    list_editable = ('quantity',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
