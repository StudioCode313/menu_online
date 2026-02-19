from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Tabel

def menu_list(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu/menu.html', {'categories': categories})

def menu_view(request, tabel_slug):
    tabel = get_object_or_404(Tabel, slug=tabel_slug,  is_active=True)
    foods = MenuItem.objects.filter(is_available=True)
    context = {
        'foods': foods,
        'tabel': tabel,
    }
    return render(request, 'menu/menu.html', context)
