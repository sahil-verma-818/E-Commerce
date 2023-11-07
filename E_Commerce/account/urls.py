from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('account/<str:id>', views.account),
    path('register', views.register),
    path('login_user', views.login_user)
]