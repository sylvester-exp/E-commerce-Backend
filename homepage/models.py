from django.db import models
from django.conf import settings  

class Category(models.Model): 
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique= True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name  
    

class Product(models.Model):  
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)      
    created_by = models.ForeignKey( settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='homepage_products')   
    prod_title = models.CharField(max_length= 255)
    company = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)



    class Meta: 
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.prod_title   
        
