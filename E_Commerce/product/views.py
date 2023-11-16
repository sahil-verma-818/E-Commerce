from django.shortcuts import render, redirect
from .models import Product, Wishlist,product_category
from account.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime
# Create your views here.

def home(request):
    category = product_category.objects.all()
    if request.method == 'GET':
        search_input = request.GET.get('search-input')
        if search_input:
            data = Product.objects.filter(product_name__icontains=search_input)
        else:
            data = Product.objects.all()

    context = {
        'data' : data,
        'category' : category
    }
    
    return render(request, 'product_template/index.html', context=context)

def product_details(request, id):

    data = Product.objects.get(id=id)
    category = product_category.objects.all()
    category_list = Product.objects.filter(category=data.category)[:3]
    context = {
        'data' : data,
        'category' : category,
        'category_list' : category_list
    }
    
    return render(request, 'product_template/detail.html', context)

def product_categories(request, category):

    product_data = Product.objects.filter(category=category)
    category_data = product_category.objects.all()
    p = Paginator(product_data, 2)
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        'product_data' : page_obj,
        'category_data' : category_data
    }
    
    return render(request, 'product_template/category.html', context)


@login_required(login_url='/register')
def wishlist(request,id):
    data = Wishlist.objects.filter(user=User.objects.get(username=id))
    context = {
        'data':data
    }
    return render(request, 'product_template/customer-wishlist.html', context)


@login_required(login_url='/register')
def addWishlist(request, uname, id):
    
    item = Wishlist.objects.filter(user=User.objects.get(id=request.user.id)).filter(product=Product.objects.get(id=id))
    if item:
        messages.error(request, "Item is already available in wishlist")
    else:
        Wishlist.objects.create(user=request.user, product=Product.objects.get(id=id), date=datetime.datetime.now)
    return redirect(f"/wishlist/{request.user}")


def addProduct(request):

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_cat = request.POST.get('product_category')
        product_desc = request.POST.get('product_desc')
        product_price = request.POST.get('product_price')
        product_stock = request.POST.get('product_stock')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')

        # print(image1)
        # print(image2)
        # print(image3)
        # print(image4)
        # print(image5)

        a, status = product_category.objects.get_or_create(category=product_cat)
        Product.objects.create(product_name=product_name, product_desc=product_desc, category=a,price=product_price,user=User.objects.get(id=request.user.id), stock_quantity=product_stock, image1=image1, image2=image2, image3=image3)
    return render(request, 'product_template/add-product.html')