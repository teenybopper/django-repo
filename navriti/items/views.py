from django.shortcuts import render, get_object_or_404
from .models import Items

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Items, id=pk)
    related_items = Items.objects.filter(Category  = item.Category, is_sold = False).exclude(pk=pk)[0:3]
    context ={
        'item' : item,
        'related_items' : related_items
    }
    
    return render(request, 'detail.html', context)




def items(request):
    query = request.GET.get('query', '')
    items = Items.objects.filter(is_sold = False)
    if query:
        items = items.filter(name__icontains = query )
    context = {
        'items' : items,
        'query' : query 
    }
    return render(request, 'search.html', context)


