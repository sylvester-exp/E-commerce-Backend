"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.contrib.auth import views as auth_views

def api_home(request):

    """
    API root endpoint: returns a JSON message directing the client to login/register endpoints.
    
    """
    
    return JsonResponse({"message": "Welcome to the Login API. Use /api/auth/login/ to authenticate."})


urlpatterns = [
    # admin site 
    path('admin/', admin.site.urls),
    # authentication endpoints
    path('api/auth/', include('store.auth_urls')),
    # application URLs
    path('', include('store.urls')), 
    path('', include('homepage.urls')), # default homepage
    path('api/cart/', include('cart.urls', namespace='cart')),

    # password setup/recovery
    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'
        ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ), name='password_reset_complete'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
