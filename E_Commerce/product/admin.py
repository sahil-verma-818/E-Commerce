from django.contrib import admin
from .models import Product,Wishlist, Review,product_category

# Register your models here.

admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(product_category)