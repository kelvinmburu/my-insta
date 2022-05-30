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
    images = Image.objects.filter(category=category)
    
    context = {}
    context['images'] = images
        
    return render(request, '', context)
