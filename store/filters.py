import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    colour = django_filters.CharFilter(field_name='colour', lookup_expr= 'iexact')
    color  = django_filters.CharFilter(field_name='colour', lookup_expr='iexact')   # alias for US spelling

    class Meta:
        model = Product
        fields = {
            'price':    ['gte', 'lte'],
            'in_stock': ['exact'],
            'subcategory': ['exact', 'icontains'],
            'usage':    ['exact', 'icontains'],   
            'colour':     ['exact', 'icontains'],
           
        }