from django.db import models
from account.models import User
from product.models import Product

# Create your models here.

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.user.username

   
class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.user.username + " " + self.product.product_name