from django.contrib import admin
from .models import Product,wishlist, Review

# Register your models here.

admin.site.register(Product)
admin.site.register(wishlist)
admin.site.register(Review)