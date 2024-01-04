from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils import timezone

# Create your models here.

user_choices = (
    ('seller', 'seller'),
    ('admin', 'admin'),
    ('customer', 'customer'),
)

address_choice = (
    ('home', 'Home'),
    ('work', 'Work'),
)

# User table with inherited abstract user.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True)
    user_type = models.CharField(max_length=10, choices=user_choices, blank=True)
    profile_pic = models.ImageField(upload_to='static/', default='./static/default_profile_pic.webp', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self) -> str:
        return self.username


# Address table to store information of addresses of users.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.PositiveBigIntegerField()
    address_type = models.CharField(max_length=10, choices=address_choice)
    primary = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.house + " " + self.area
    

class otp_validation(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()
    context = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        self.expires_at = timezone.now() + timezone.timedelta(minutes=5)

    






