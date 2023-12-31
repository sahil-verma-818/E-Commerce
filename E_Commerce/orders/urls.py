from django.urls import path
from . import views

urlpatterns = [
    path('orders/<str:id>', views.order),
    path('order-details/<str:uname>/<int:id>', views.order_details),
    path('checkout/<str:id>', views.checkout),
    path('admin-panel/dashboard', views.admin_home),
    path('admin-order/<str:uname>/<int:id>', views.admin_order),
    path('update-status/<int:id>', views.update_status),
    path('payment-success/<int:id>', views.payment_success),
    path('payment_failure/', views.payment_failure)


]