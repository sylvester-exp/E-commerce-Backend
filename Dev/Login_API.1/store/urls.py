from django.urls import path
from .views import LoginView  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from . import views

app_name = 'store'

urlpatterns= [
    path('', views.all_products, name= 'all_products'),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]