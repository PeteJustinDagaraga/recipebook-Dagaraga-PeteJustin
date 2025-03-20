from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile
from django.contrib.auth.models import User

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name',)
    list_filter = ('name',)
    list_display_links = None
    list_editable = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name','author__name',)
    list_filter = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('quantity','ingredient__name',)
    list_filter = ('recipe__name',)
    search_fields = ['ingredient__name','recipe__name']
    list_display_links = None
    list_editable = ('quantity',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
