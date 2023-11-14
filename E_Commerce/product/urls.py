from django.urls import path
from . import views



urlpatterns = [
    path('product/<str:id>', views.product_details),
    path('wishlist/<str:id>', views.wishlist),
    path('product_category/<str:category>', views.product_categories)
]