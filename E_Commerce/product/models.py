from account.models import User
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.


# Model for product Category
class ProductCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category
    


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.brand_name


class Color(models.Model):
    color_name = models.CharField(max_length=255, primary_key=True)

    def __str__(self) -> str:
        return self.color_name



class Mdl(models.Model):
    mdl = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.mdl



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True) 
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    mdl = models.ForeignKey(Mdl, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    image1 = models.ImageField(upload_to = 'static/')
    image2 = models.ImageField(upload_to = 'static/')
    image3 = models.ImageField(upload_to = 'static/')
    image4 = models.ImageField(upload_to = 'static/', blank=True)
    image5 = models.ImageField(upload_to = 'static/', blank=True)

    def __str__(self) -> str:
        return self.product_name
    


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.product_name

class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    heading = models.CharField(max_length=100)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.product.product_name