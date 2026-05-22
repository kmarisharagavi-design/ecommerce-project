# orders/models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    ordered_at = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.user.username}"