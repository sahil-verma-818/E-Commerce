from django.shortcuts import render
from .models import CartItems
from account.models import User

# Create your views here.

def cartlist(request,id):

    data = CartItems.objects.filter(user=User.objects.get(username=id))
    context = {
        'data' : data
    }

    return render(request, 'cart_template/basket.html', context)   