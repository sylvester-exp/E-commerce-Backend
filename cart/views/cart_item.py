from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer
from store.models import Product



"""""
Manages cart items for authenticated users. Supports listing, adding, and removing items from the shopping cart.
"""""

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        product = Product.objects.get(pk=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)


class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        try:
            product = Product.objects.get(pk=product_id)
            cart = Cart.objects.get(user=request.user)
            CartItem.objects.filter(cart=cart, product=product).delete()
            return Response({"detail": "Item removed from cart."})
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=404)

class ListCartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
