from django.contrib import admin
from store.models import Product
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

class ProductResource(resources.ModelResource):
    prod_title = fields.Field(attribute='prod_title', column_name='ProductTitle')
    usage = fields.Field(attribute='usage', column_name='Usage')
    image = fields.Field(attribute='image', column_name='ImageURL')
    price = fields.Field(attribute='price', column_name='Price')
    subcategory = fields.Field(attribute='subcategory', column_name='SubCategory')
    colour = fields.Field(attribute='colour', column_name='Colour')

    class Meta:
        model = Product
        fields = ('prod_title', 'usage', 'image', 'price', 'subcategory', 'colour')
        import_id_fields = ('prod_title',) 

class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
