from django.shortcuts import render

# Create your views here.

def product_category(request, id):
    
    return render(request, 'product_template/index.html')

def wishlist(request):

    return render(request, 'product_template/customer_wishlist.html')