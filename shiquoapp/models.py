from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(default='example@example.com')  # Add a default value here
    address = models.CharField(max_length=255, null=True, blank=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.id} by {self.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Ensure this field exists
    cart_item = models.CharField(max_length=255, default='default_cart_item')  # Ensure this field exists

    def __str__(self):
        return f"{self.quantity} of {self.product.name} at {self.price_at_order} each"

class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
from django.db import models
from django.core.validators import MinValueValidator

class MpesaResponseBody(models.Model):
    body = models.JSONField()

class Transaction(models.Model):
    phonenumber = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    receipt_no = models.CharField(max_length=100)

    def __str__(self):
        return self.receipt_no