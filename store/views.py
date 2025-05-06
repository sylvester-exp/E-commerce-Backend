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
    GET /products/ - returns a filtered, paginated list of products.
     Query parameters: 
     - ?in_stock=true/false
      - ?price_min=
      - ?price_max=
      - ?sort=price|prod_title|category
    """
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPageNumberPagination

    def get_queryset(self):
        queryset = Product.objects.all()
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
    
    def get(self, request):
        queryset = Product.objects.all()

        # Sorting logic
        sort_param = request.GET.get('sort') 
        allowed_sort_fields = ['price', 'prod_title', 'created']

        if sort_param:
            sort_field = sort_param.lstrip('-')
            if sort_field in allowed_sort_fields:
                queryset = queryset.order_by(sort_param)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
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