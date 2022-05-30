from django.test import TestCase
from .models import Category,Image
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        # Creating an image and saving it
        self.image1 = Image(description='lorem ipsum dolor sit amet, consectetur adipiscing', altText='Food Illustration', hashtags='#food')
        self.image1.save.image()
        
        # Creating a new category
        self.new_category = Category(name='testing')
        self.new_category.save()
        
        
    def tearDown(self):
        Category.objects.all().delete()
        
        