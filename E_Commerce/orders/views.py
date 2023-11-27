from django.shortcuts import render
from .models import Order, OrderItems
from account.models import User
from django.contrib.auth.decorators import login_required
from product.models import ProductCategory

# Create your views here.


# Functionality to render order items to any user
@login_required
def order(request, id):
    price = {}
    data = Order.objects.filter(user=User.objects.get(username=id))
    
    # Calculation of gross price for any user
    for x in data:
        sum = 0
        items = OrderItems.objects.filter(order=x)
        for y in items:
            sum += y.product.price * y.quantity
        price[x.id] = sum

    context = {
        'data' : data,
        'price' : price,
        'category' : ProductCategory.objects.all()
    }
    return render(request, 'order_template/customer-orders.html', context)


@login_required(login_url='/register')
def checkout1(request,id):
    

    return render(request, 'order_template/checkout1.html')