from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from store.models import Product
from cart.models import CartItem
from cart.models import Cart
from django.contrib.auth import get_user_model

User = get_user_model()

class CartAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
    email='test@example.com',
    password='testpass'
)
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            prod_title='Test Product',
            price=9.99,
            in_stock=True,
        )
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_add_to_cart(self):
        url = reverse('cart:add-to-cart')
        response = self.client.post(url, {
            "product_id": self.product.id,
            "quantity": 3
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CartItem.objects.count(), 1)

    def test_view_cart(self):
        url = reverse('cart:cart-detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_clear_cart(self):
        url = reverse('cart:cart-clear')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
