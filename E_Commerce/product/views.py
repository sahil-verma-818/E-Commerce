from django.shortcuts import render
from .models import Product, Wishlist
from account.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.



def product_category(request, id):

    data = Product.objects.get(id=id)
    context = {
        'data' : data,
        'user' : request.user
    }
    
    return render(request, 'product_template/detail.html', context)



def wishlist(request,id):
    data = Wishlist.objects.filter(user=User.objects.get(username=id))
    context = {
        'data':data
    }
    return render(request, 'product_template/customer-wishlist.html', context)