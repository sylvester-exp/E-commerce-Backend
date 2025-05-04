from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Category
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'prod_title',
            'price',
            'image',
            'in_stock',
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
                  'id',
                  'prod_title', 
                  'usage', 
                  'image', 
                  'price', 
                  'subcategory', 
                  'colour',
        ]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['role'] = user.role  # Optional: include role in token
        return token
    
def validate(self, attrs):
    email = attrs.get("email")
    password = attrs.get("password")

    user = authenticate(username=email, password=password)

    if user is None:
        raise serializers.ValidationError("Invalid email or password")

    refresh = self.get_token(user)
    
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


    

