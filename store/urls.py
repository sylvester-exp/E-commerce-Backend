from django.urls import path
from .views import LoginView  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import RegisterView
from .views import HomePageProductListView


app_name = 'store'

urlpatterns = [
    path('products/homepage/', HomePageProductListView.as_view(), name='homepage_products'),
    path('products/home/', HomePageProductListView.as_view(), name='home_products'),
    path('', views.all_products, name='all_products'),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),  
]
