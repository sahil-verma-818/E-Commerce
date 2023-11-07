from django.urls import path
from . import views



urlpatterns = [
    path('product/<str:id>', views.product_category),
    path('wishlist/', views.wishlist)
]