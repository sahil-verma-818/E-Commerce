from django.urls import path
from . import views

urlpatterns = [
    path('orders/<str:id>', views.order),
    path('order-details/<str:uname>/<int:id>', views.order_details),
    path('checkout/<str:id>', views.checkout),
    path('admin-panel/dashboard', views.admin_home),

]