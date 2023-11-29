from django.shortcuts import render
from .models import Order, OrderItems
from account.models import User
from django.contrib.auth.decorators import login_required
from product.models import ProductCategory
from cart.models import CartItems

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
def checkout(request,id):

    if request.method == 'GET':
        total = 0
        data = CartItems.objects.filter(user=User.objects.get(id=request.user.id))
        
        # Calculating gross price for the whole cart of the user
        for x in data:
            total += x.product.price * x.quantity
        context = {
            'data' : data,
            'total' : total
        }

        return render(request, 'order_template/checkout.html', context)
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        house = request.POST.get('house')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        payment_method = request.POST.get('payment-method')

        cart = CartItems.objects.filter(user=request.user.id)

        

        return render(request, 'order_template/checkout.html')
