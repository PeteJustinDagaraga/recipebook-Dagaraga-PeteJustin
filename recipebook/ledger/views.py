from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

fullcontext = {
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
                    "quantity": "1 cup"
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

def recipeList(request):
    ctx = fullcontext
    return render(request, "recipeList.html", ctx)

def recipeEntry(request,num=-1):
    if num in range(1,3):
        ctx = fullcontext["recipes"][num-1]
    else:
        return HttpResponse(loader.get_template("404.html").render())
    return render(request, "recipeEntry.html", ctx)
