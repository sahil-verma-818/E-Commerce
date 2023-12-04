from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import CartItems
from account.models import User
from product.models import Product, ProductCategory
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

# Functionality of rendering cartlist
@login_required(login_url='/register')
def cartlist(request,id):
    
    if request.method == 'GET':
        total = 0
        data = CartItems.objects.filter(user=request.user)
        
        # Calculating gross price for the whole cart of the user
        for x in data:
            if request.GET.get(f"{x.id}"):
                x.quantity = request.GET.get(f"{x.id}")
                messages.success(request, "Cart Information Updated Successfully !!")
                x.save()
            total += x.product.price * int(x.quantity)
        context = {
            'data' : data,
            'total' : total,
            'category' : ProductCategory.objects.all()
        }

        return render(request, 'cart_template/basket.html', context)
            


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
    messages.success(request, "Success !! item added to cart")
    return redirect(f"/cart/{request.user}")


# Functionality to remove items from the cart
@login_required(login_url='/register')
def remove_cart(request, uname, id):
        if request.user == User.objects.get(username=uname):
            CartItems.objects.get(id=id).delete()
            messages.success(request, "Item removed from the cart")
            return redirect(f"/cart/{request.user}")
        
