from django.shortcuts import render
from .models import Product
# Create your views here.

def product_category(request, id):

    data = Product.objects.get(id=id)
    context = {
        'data' : data
    }
    
    return render(request, 'product_template/detail.html', context)

def wishlist(request):

    return render(request, 'product_template/customer_wishlist.html')