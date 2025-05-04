from rest_framework import serializers
from store.models import Product
from django.conf import settings

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
           'Gender', 'Category', 'ProductType', 'Colour',
            'Usage', 'ProductTitle', 'Image', 'ImageURL',
            'price', 
        ]

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='prod_title')

    class Meta:
        model = Product
        fields = [
             'prod_title', 'usage', 'image', 'price', 'subcategory', 'colour' 
        ]

class BulkProductSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)  

    def create(self, validated_data):
        product_data = validated_data['products']
        products = [Product(**item) for item in product_data]
        return Product.objects.bulk_create(products)
