from django.urls import path
from store import views
from homepage.views import HomePageProductListAPIView, HomePageProductListView, HomePageView
from store.views import ProductListAPIView
from homepage.views import HomePageProductListView  
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='homepage'),
    path('', views.all_products, name='all_products'),
    path('products/', ProductListAPIView.as_view(), name='all_products'),
    path('products/homepage/', HomePageProductListView.as_view(), name='homepage_products'),
    path('products/home/', HomePageProductListView.as_view(), name='home_products'),
    path('products/', HomePageProductListAPIView.as_view(), name='homepage-products'),
]
