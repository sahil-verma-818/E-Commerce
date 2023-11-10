from django.shortcuts import render
from .models import Order, OrderItems
from account.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def order(request, id):
    price = {}
    data = Order.objects.filter(user=User.objects.get(username=id))
    for x in data:
        print(x)
        sum = 0
        items = OrderItems.objects.filter(order=x)
        for y in items:
            sum += y.product.price * y.quantity
        price[x.id] = sum

    context = {
        'data' : data,
        'price' : price
    }
    
    

    return render(request, 'order_template/customer-orders.html', context)