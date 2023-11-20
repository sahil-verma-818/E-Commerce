from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('product/<str:id>', views.product_details),
    path('wishlist/<str:id>', views.wishlist),
    path('addWishlist/<str:uname>/<int:id>', views.addWishlist),
    path('removeWishlist/<str:uname>/<int:id>', views.removeWishlist),
    path('product_category/<str:category>', views.product_categories),
    path('add-product/<str:id>', views.addProduct),

]