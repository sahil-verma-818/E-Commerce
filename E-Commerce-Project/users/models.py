from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

user_choices = (
    ('seller', 'seller'),
    ('admin', 'admin'),
    ('user', 'user'),
)

address_choice = (
    ('home', 'Home')
    ('work', 'Work')
)

class Address(models.Model):
    house = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.PositiveBigIntegerField()
    address_type = models.CharField(max_length=10, choices=address_choice)

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=user_choices, blank=True)



