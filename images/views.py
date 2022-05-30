from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    categories = Category.objects.all()
    
    context = {}
    context['categories'] = categories
    return render(request, 'main/index.html', context)


def category_page(request, slug):
    
    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('date_created')
    
    for x in images:
        x.short_description = x.description[:130]
    
    context = {}
    context['images'] = images
    context['category'] = category
        
    return render(request, 'main/category.html', context)
