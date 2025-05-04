from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Category, Product

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

        fields = ('id',
                  'prod_title', 
                  'usage', 
                  'image', 
                  'price', 
                  'subcategory', 
                  'colour')
        
        

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    
    list_display = ['prod_title', 
                  'usage', 
                  'image', 
                  'price', 
                  'subcategory', 
                  'colour']











