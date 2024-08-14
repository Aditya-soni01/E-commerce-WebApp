from django.db import models
from django.contrib.auth.models import User
from .order import Order
import uuid

class ShippingAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_address')
    address = models.TextField()
    city = models.CharField(max_length=100)
    postel_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'Shipping Address For Order {self.order.id}'