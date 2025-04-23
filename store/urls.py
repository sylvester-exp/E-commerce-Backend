from django.urls import path,
from .views import LoginView  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from users.views import CustomTokenObtainPairView


app_name = 'store'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),  
   # path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
