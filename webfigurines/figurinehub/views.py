from django.shortcuts import render
from .models import Figurine

def index(request):
    return render(request, 'index.html')

def catalogue(request):
    figurines = Figurine.objects.all()
    
    # Поиск
    search = request.GET.get('search')
    if search:
        figurines = figurines.filter(name__icontains=search)
    
    # Сортировка
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        figurines = figurines.order_by('price')
    elif sort == 'price_desc':
        figurines = figurines.order_by('-price')
    elif sort == 'name_asc':
        figurines = figurines.order_by('name')
    elif sort == 'name_desc':
        figurines = figurines.order_by('-name')
    
    context = {
        'figurines': figurines,
        'search': search,
        'sort': sort,
    }
        
    return render(request, 'catalogue.html', context)