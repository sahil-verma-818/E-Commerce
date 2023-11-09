from django.shortcuts import render, redirect
from .models import CartItems
from account.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def cartlist(request,id):
    total = 0
    data = CartItems.objects.filter(user=User.objects.get(username=id))
    for x in data:
        total += x.product.price * x.quantity
    context = {
        'data' : data,
        'total' : total
    }

    return render(request, 'cart_template/basket.html', context)

@login_required
def remove_cart(request, uname, id):
        print(request.user)
        print(User.objects.get(username=uname))
        if request.user == User.objects.get(username=uname):
            data = CartItems.objects.get(id=id).delete()
            return redirect(f"cart/{uname}")