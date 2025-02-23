from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def recipeList(request):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3pcs"
                        },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                        },
                    {
                        "name": "pork",
                        "quantity": "1kg"
                        },
                    {
                        "name": "water",
                        "quantity": "1L"
                        },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                        }
                    ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                        },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                        },
                    {
                        "name": "vinegar",
                        "quantity": "1/2cup"
                        },
                    {
                        "name": "water",
                        "quanity": "1 cup"
                        },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                        },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                        },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                        }
                    ],
                "link": "/recipe/2"
                }
            ]
        }
    return render(request, "recipeList.html", ctx)

def recipe1(request):
    return HttpResponse("This is where the Recipe1.html should be")

def recipe2(request):
    return HttpResponse("This is where the Recipe2.html should be")
