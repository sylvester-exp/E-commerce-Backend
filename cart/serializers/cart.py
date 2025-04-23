from rest_framework import serializers
from cart.models import Cart
from .cart_item import CartItemSerializer  # use relative import



class CartSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

class Meta:
        model = Cart
        fields = ['id', 'user', 'items']