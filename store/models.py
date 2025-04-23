from django.db import models
from django.conf import settings  
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager




class Category(models.Model): 
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique= True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name  




class Product(models.Model):
    prod_title = models.CharField(max_length=255)
    usage = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)  # Use ImageField if you plan file uploads
    price = models.DecimalField(max_digits=8, decimal_places=2)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    colour = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    class Meta: 
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.prod_title   
        

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  # Remove username

    USERNAME_FIELD = 'email'  # Set email as the login field
    REQUIRED_FIELDS = []  # Remove username requirement

    objects = CustomUserManager()


    def __str__(self):
        return self.email
    

class Cart(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='store_carts'  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.user.username})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='store_cart_cart_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        from store.models import Product
        return f"{self.quantity} x {self.product.title}"

    def get_total_price(self):
        from store.models import Product
        return self.product.price * self.quantity