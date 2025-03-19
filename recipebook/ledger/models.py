from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User    

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return '/ingredient/{}'.format(self.name)

    class Meta:
        ordering = ['name']
        unique_together = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'author')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("ledger:recipeEntry",kwargs={"num":int(self.name[7:])})

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE, related_name = 'recipe')
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = 'ingredient')
