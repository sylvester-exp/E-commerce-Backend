from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import LoginView
from .views import RegisterView

urlpatterns = [
  path("login/",     LoginView.as_view(),               name="login"),
  path("register/",  RegisterView.as_view(),            name="register"),
  path("token/refresh/",          TokenRefreshView.as_view(), name="token_refresh"),
  path("token/",    TokenObtainPairView.as_view(),       name="token_obtain_pair"),
 ]
