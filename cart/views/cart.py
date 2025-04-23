from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework.exceptions import NotFound

class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class CartClearView(APIView):
    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            raise NotFound("Cart does not exist.")
        
        cart.items.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
