from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView
from django.urls import include
from .views import ProductListAPIView, ProductDetailAPIView
from homepage.views import HomePageProductListView

app_name = 'store'

urlpatterns = [
    path('api/auth/', include('store.auth_urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('products/', ProductListAPIView.as_view(),   name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/products/', HomePageProductListView.as_view(), name='product-list'),
]
