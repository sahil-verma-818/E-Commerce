from product.models import Product
from users.models import Address
from django.db import models
from django.conf import settings


# Create your models here.

User = settings.AUTH_USER_MODEL

payment_choices = (
    ('COD', 'Cash on Delivery'),
    ('net banking', 'net banking'),
    ('upi', 'UPI'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItems')
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_method = models.CharField(max_length=20, choices=payment_choices)
    is_confirmed = models.BooleanField(default=False)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
