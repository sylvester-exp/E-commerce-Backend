from django.shortcuts import render
from .models import Category, Product
from .serializers import RegisterSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import ProductListSerializer

def companies(request):
    return { 
        'companies': Category.objects.all
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")  # Changed from username to email
        password = request.data.get("password")
        user = authenticate(email=email, password=password)


        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        return Response({"error": "Invalid credentials"}, status=400)


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class HomePageProductListView(ListAPIView):
    queryset = Product.objects.filter(is_active=True, in_stock=True).order_by('-created')
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    pagination_class = None