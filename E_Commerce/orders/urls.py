from django.urls import path
from . import views

urlpatterns = [
    path('orders/<str:id>', views.order),
    path('checkout1/<str:id>', views.checkout1)
]