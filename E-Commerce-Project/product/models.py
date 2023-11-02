from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    image1 = models.ImageField(upload_to = 'static/')
    image2 = models.ImageField(upload_to = 'static/')
    image3 = models.ImageField(upload_to = 'static/')
    image4 = models.ImageField(upload_to = 'static/')
    image5 = models.ImageField(upload_to = 'static/')

class wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
