from rest_framework import serializers
from .models import Product, Category
from django.conf import settings

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'prod_title',
            'company',
            'price',
            'image',
            'slug',
            'in_stock',
        ]

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'created_by', 'prod_title', 'company',
            'description', 'image', 'slug', 'price',
            'in_stock', 'is_active', 'created', 'updated'
        ]