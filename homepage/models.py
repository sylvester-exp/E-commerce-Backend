from django.db import models
from django.conf import settings  

""""
A category for grouping products on the homepage (e.g shoes, shirts).

"""""
class Category(models.Model): 
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique= True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        # return a readable representation
        return self.name  
    

