from django.urls import path
from . import views



urlpatterns = [
    path('cart/<str:id>', views.cartlist),
    path('cart/add/<int:id>/<str:uname>', views.add_cart),
    path('remove-cart/<str:uname>/<int:id>', views.remove_cart) 
]