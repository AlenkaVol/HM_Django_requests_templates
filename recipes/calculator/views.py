from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def list_recipes(request):
    recipes = DATA
    return render(request, 'calculator/list.html', {'recipes': recipes})


def recipes(request, recipe):
    servings = int(request.GET.get('servings', 1))
    recipe_data = DATA.get(recipe, None)
    if recipe in DATA.keys():
        for ingredient in recipe_data:
            recipe_data[ingredient] = recipe_data[ingredient] * servings
        context = {
            'recipe': recipe_data,
            'recipe_name': recipe,
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Такого рецепта нет!')