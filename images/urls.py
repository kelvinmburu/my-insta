from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/category/<slug:slug>', views.category_page, name='image_category')
]