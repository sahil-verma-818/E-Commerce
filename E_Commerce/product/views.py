from django.shortcuts import render
from .models import Product, Wishlist,product_category
from account.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger 
# Create your views here.



def product_details(request, id):

    data = Product.objects.get(id=id)
    context = {
        'data' : data,
        'user' : request.user
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



def wishlist(request,id):
    data = Wishlist.objects.filter(user=User.objects.get(username=id))
    context = {
        'data':data
    }
    return render(request, 'product_template/customer-wishlist.html', context)