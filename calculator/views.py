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
    # можете добавить свои рецепты ;)
}


def recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': dict()}
    if dish in DATA.keys():
        for key, value in DATA[dish].items():
            context['recipe'][key] = value * servings
        return render(request, 'calculator/index.html', context)
    else:
        return render(request, 'calculator/index.html', context)

