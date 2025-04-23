from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug' : ('name',)}


    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ['prod_title', 'price', 'created', 'in_stock']
        list_filter = ['price','in_stock']
        list_editable = ['price', 'in_stock']
        search_fields = ('prod_title',)
        #prepopulated_fields = {'slug': ('prod_title',)}











