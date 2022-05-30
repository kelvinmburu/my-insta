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
    images = Image.objects.filter(category=category).order_by('date_created')[:6]
    
    for x in images:
        x.short_description = x.description[:130]
    
    context = {}
    context['images'] = images
    context['category'] = category
        
    return render(request, 'main/category.html', context)


def image_detail_page(request, slug1, slug2):
    
    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)
    
    context = {}
    context['category'] = category
    context['image'] = image
    
    return render(request, 'main/image.html', context)