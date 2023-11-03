from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('user/account', views.account)
]