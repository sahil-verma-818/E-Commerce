from django.urls import path
from . import views



urlpatterns = [
    path('<str:id>', views.product_category),
    path('wishlist/', views.wishlist)
]