from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:id>', views.account),
    path('register', views.register),
    path('login_user', views.login_user),
    path('update_password/<str:id>', views.update_password),
    path('logout/<str:id>', views.logout_user),
    path('admin-panel/dashboard', views.admin_home),
    path('adminlogin', views.admin_login),
    path('adminRegister', views.admin_register),
    path('adminProfile/<str:id>', views.account)
]