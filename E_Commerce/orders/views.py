from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Order, OrderItems
from account.models import User, Address
from django.contrib.auth.decorators import login_required
from product.models import ProductCategory,Product
from cart.models import CartItems
from django.contrib import messages
import datetime
from django.db.models import Q


# Create your views here.


# Functionality to render order items to any user
@login_required
def order(request, id):
    price = {}
    data = Order.objects.filter(user=request.user)
    
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
def order_details(request, uname, id):
    
    order = Order.objects.get(id=id)
    order_items = OrderItems.objects.filter(order=order)
    try:
        invoice_address = Address.objects.get(Q(user=request.user) & Q(primary=True))
    except Address.DoesNotExist:
        invoice_address = None

    context = {
        'order' : order,
        'order_items' : order_items,
        'invoice' : invoice_address
    }
    print(request.user.user_type)

    return render(request, 'order_template/customer-order.html', context)


@login_required(login_url='/register')
def checkout(request,id):

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

        return render(request, 'order_template/checkout.html', context)
    if request.method == 'POST':

        order_address = {
        'house' : request.POST.get('house'),
        'area' : request.POST.get('area'),
        'landmark' : request.POST.get('landmark'),
        'zip' : request.POST.get('zip'),
        'state' : request.POST.get('state'),
        'city' : request.POST.get('city'),
        'user' : request.user,
        'address_type' : request.POST.get('address-type')
        }
        payment_method = request.POST.get('payment-method')
        shipping_address, status = Address.objects.get_or_create(**order_address)
        cart_data = CartItems.objects.filter(user=request.user)
        order = Order.objects.create(user=request.user, delivery_address=shipping_address, order_date=datetime.datetime.now(), payment_method=payment_method)
        total = 0
        for data in cart_data:
            stock_remain=Product.objects.get(id=data.product.id)
            if stock_remain.stock_quantity >= data.quantity:
                OrderItems.objects.create(order=order, product=data.product, quantity=data.quantity)
                stock_remain.stock_quantity -= data.quantity
                stock_remain.save()
                total += data.product.price
                data.delete()
            else:
                messages.error(request, f"Stock Insufficient !! You can only order {data.product} only a maximum of {stock_remain.stock_quantity}")
  
        order.total_bill=total
        if OrderItems.objects.filter(order=order):
            order.save()
            messages.success(request, "Order Placed")
            return redirect(f"/orders/{request.user}")
        else:
            order.delete()
            messages.error(request, "Order can't be placed due to unavailability of items")
        
    


# ----------------------- Admin Panel -----------------------------

@login_required(login_url='/adminlogin')
def admin_home(request):
    return render(request, 'admin_template/index.html', {'order_detail' : OrderItems.objects.filter(product__user=request.user)})


def admin_order(request, uname, id):
    order = Order.objects.get(id=id)
    order_items = OrderItems.objects.filter(order=order)
    try:
        invoice_address = Address.objects.get(Q(user=order.user.id) & Q(primary=True))
    except Address.DoesNotExist:
        invoice_address = None

    context = {
        'order' : order,
        'order_items' : order_items,
        'invoice' : invoice_address
    }
    return render(request, 'admin_template/order-detail.html', context)

def update_status(request, id):
    
    if request.method == 'POST':
        status = request.POST.get('selectedOption')
        order = OrderItems.objects.get(id=id)
        order.status=status
        order.save()
        confirmation=OrderItems.objects.filter(order=order.order)
        for data in confirmation:
            if data.status != 'delivered':
                break
        else:
            cnf=Order.objects.get(id=order.order.id)
            cnf.is_delivered=True
            cnf.save()


