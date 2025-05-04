from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from store.serializers import ProductListSerializer
from store.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Product
from rest_framework import generics, filters
from django.http import JsonResponse
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render


def home_page_view(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, 'store/home.html', {'products': products})

class HomePageView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Welcome to the Homepage API"})
    
class HomePageProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(in_stock=True).order_by('-created')
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    pagination_class = None

     # filtering, search, pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'in_stock', 'price']
    search_fields = ['prod_title', 'description', 'company']
    ordering_fields = ['price', 'created', 'updated']

class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class HomePageProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.filter(in_stock=True).order_by('-created')
    

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
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
        queryset = Product.objects.filter(in_stock=True)

        # sorting logic
        sort_param = request.GET.get('sort') 
        allowed_sort_fields = ['price', 'prod_title', 'created']

        if sort_param:
            sort_field = sort_param.lstrip('-')
            if sort_field in allowed_sort_fields:
                queryset = queryset.order_by(sort_param)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to the Homepage API"})
