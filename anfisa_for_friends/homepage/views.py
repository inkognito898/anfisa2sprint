from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    ice_cream_list = IceCream.objects.values(
        'id',
        'title',
        'description',
        'price'
        ).filter(Q(is_published=True) & Q(is_on_main=True) & Q(category__is_published=True))
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
