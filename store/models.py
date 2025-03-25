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
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)      
    created_by = models.ForeignKey( settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='store_products')   
    prod_title = models.CharField(max_length= 255)
    company = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)



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
    

