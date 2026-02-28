from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Tabel

def menu_list(request):
    categories = Category.objects.prefetch_related('items').all()
    tabel = Tabel.objects.all()
    context = {
        'categories': categories,
        'tables': tabel,
    }
    return render(request, 'menu/menu.html', context)

def menu_view(request, tabel_slug):
    tabel = Tabel.objects.get(number=tabel_slug)
    foods = MenuItem.objects.filter(is_available=True)
    context = {
        'foods': foods,
        'tables': tabel,
    }
    return render(request, 'menu/menu.html', context)
