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
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

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

class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class HomePageProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.filter(is_active=True, in_stock=True).order_by('-created')
    

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        company = self.request.query_params.get('company')
        in_stock = self.request.query_params.get('in_stock')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')

        if category:
            queryset = queryset.filter(category__name__iexact=category)

        if company:
            queryset = queryset.filter(company__icontains=company)

        if in_stock:
            queryset = queryset.filter(in_stock=in_stock.lower() == 'true')

        if price_min:
            queryset = queryset.filter(price__gte=price_min)

        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset