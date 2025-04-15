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
    prod_title = models.CharField(max_length=255)
    usage = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)  # Use ImageField if you plan file uploads
    price = models.DecimalField(max_digits=8, decimal_places=2)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    colour = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)



    class Meta: 
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.prod_title   
        
