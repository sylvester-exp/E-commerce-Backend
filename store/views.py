"""
store.views
-----------
contains API views for listing products, handling login/register etc.

"""
from django.shortcuts import render
from .models import Category, Product
from .serializers import RegisterSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from store.serializers import ProductSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import RetrieveAPIView
from homepage.serializers import ProductListSerializer
from homepage.views import ProductPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from homepage.views import ProductPageNumberPagination
from .filters import ProductFilter


User = get_user_model()

def companies(request):
    return { 
        'companies': Category.objects.all
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # ← use .data, not .POST, when you send JSON
        email    = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is None:
             return Response({"error": "Invalid credentials"}, status=400)
    
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access":  str(refresh.access_token),
        })
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProductListAPIView(ListAPIView):
    """
    GET /products/ 
    Returns a filtered, paginated list of active products.

    Query params (all optional):
      - colour=<iexact>       (or color= alias)
      - usage=<icontains>
      - price__gte=<min price>
      - price__lte=<max price>
      - in_stock=true|false
      - subcategory=<iexact or contains>
    Sorting:
      - ?sort=<field> or ?sort=-<field>
        allowed sort fields: price, prod_title, created
    Pagination:
      - ?page=<n> (10 items/page by default)
    """
    queryset           = Product.objects.filter()
    serializer_class   = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class   = ProductPageNumberPagination

    # filtering and ordering setup 
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_class    = ProductFilter        
    ordering_fields    = ['price', 'prod_title', 'created']
    ordering           = ['-created']           
    ordering_param     = 'sort'         
    
class IsRetailer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'retailer'
    
class RetailerOnlyView(APIView):
    permission_classes = [IsRetailer]

    def get(self, request):
        return Response ({"message": "Retailer content"})
    
class PublicTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'pk'

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer