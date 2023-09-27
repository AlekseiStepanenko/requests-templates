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

def omlet(request):

    amount = int(request.GET.get('amount', 1))
    ingrs = []
    for ing, n in DATA['omlet'].items():
        res = n * amount
        ingrs.append(f'{ing}: {res}')

    context = {
        'omlet': ingrs,
    }

    return render(request, 'calculator/omlet.html', context)

def pasta(request):

    amount = int(request.GET.get('amount', 1))
    ingrs = []
    for ing, n in DATA['pasta'].items():
        res = n * amount
        ingrs.append(f'{ing}: {res}')

    context = {
        'pasta': ingrs,
    }

    return render(request, 'calculator/pasta.html', context)


def buter(request):

    amount = int(request.GET.get('amount', 1))
    ingrs = []
    for ing, n in DATA['buter'].items():
        res = n * amount
        ingrs.append(f'{ing}: {res}')

    context = {
        'buter': ingrs,
    }

    return render(request, 'calculator/buter.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
