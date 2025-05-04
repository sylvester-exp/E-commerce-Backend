from django.db import models
from django.conf import settings  

class Category(models.Model): 
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique= True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name  
    

