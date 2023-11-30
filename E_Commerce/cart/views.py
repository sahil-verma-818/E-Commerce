from django.shortcuts import render, redirect
from .models import CartItems
from account.models import User
from product.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.

# Functionality of rendering cartlist
@login_required(login_url='/register')
def cartlist(request,id):
    
    if request.method == 'GET':
        total = 0
        data = CartItems.objects.filter(user=request.user)
        
        # Calculating gross price for the whole cart of the user
        for x in data:
            total += x.product.price * x.quantity
        context = {
            'data' : data,
            'total' : total
        }

        return render(request, 'cart_template/basket.html', context)
    
    # Implementation of update cart functionality.
    if request.method == 'POST':
        data = CartItems.objects.filter(user=User.objects.get(username=id))

        for x in data:
            x.quantity = request.POST.get(f"{x.id}")
            x.save()

        return redirect(f"/cart/{request.user}")
            


# Functionality to implement addition of items to the cart
@login_required(login_url='/register')
def add_cart(request,uname, id):

    item = CartItems.objects.filter(user=User.objects.get(id=request.user.id)).filter(product=Product.objects.get(id=id))
    # If item is already present in cart just update the cart with a "+1" quantity
    if item:
        item[0].quantity += 1
        item[0].save()
    # Else add a new item to the cart
    else:
        CartItems.objects.create(user=request.user, product=Product.objects.get(id=id), quantity=1)
    return redirect(f"/cart/{request.user}")



# Functionality to remove items from the cart
@login_required(login_url='/register')
def remove_cart(request, uname, id):
        if request.user == User.objects.get(username=uname):
            CartItems.objects.get(id=id).delete()
            return redirect(f"/cart/{request.user}")
        
