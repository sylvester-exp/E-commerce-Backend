# cart/urls.py
from django.urls import path
from .views.cart_item import AddToCartView, RemoveFromCartView, ListCartItemsView
from .views.cart import CartDetailView, CartClearView

app_name = "cart"

urlpatterns = [
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('items/', ListCartItemsView.as_view(), name='list-cart-items'),
    path('detail/', CartDetailView.as_view(), name='cart-detail'),
    path('clear/', CartClearView.as_view(), name='cart-clear'),
]
