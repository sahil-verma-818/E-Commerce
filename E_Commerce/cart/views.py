from django.shortcuts import render

# Create your views here.

def cartlist(request,id):

    return render(request, 'cart_template/basket.html')   