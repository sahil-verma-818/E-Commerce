from product.models import Product
from django.db import models
from account.models import User, Address


# Create your models here.

payment_choices = (
    ('COD', 'Cash on Delivery'),
    ('net banking', 'net banking'),
    ('upi', 'UPI'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_method = models.CharField(max_length=20, choices=payment_choices)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.order_id


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product_name