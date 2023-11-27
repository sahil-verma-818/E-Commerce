from django.shortcuts import render, redirect
from .models import Product, Wishlist,ProductCategory,Color,Mdl, Brand
from account.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime
from django.db.models import Q

# Create your views here.

''' Rendering home page data and implementing search functionality '''
def home(request):
    category = ProductCategory.objects.all()
    if request.method == 'GET':

        # Implement search feature using product name
        search_input = request.GET.get('search-input')
        if search_input:
            product_data = Product.objects.filter(product_name__icontains=search_input)

            # Implement pagination on searching
            p = Paginator(product_data, 1)
            page_number = request.GET.get('page')

            try:
                page_obj = p.get_page(page_number)
            except PageNotAnInteger:
                page_obj = p.page(1)
            except EmptyPage:
                page_obj = p.page(p.num_pages)
            return render(request, 'product_template/category.html', {'product_data' : page_obj,})
        else:
            data = Product.objects.all()

    context = {
        'data' : data,
        'category' : category
    }
    
    return render(request, 'product_template/index.html', context=context)


''' Functionality to view complete details of any perticular product'''
def product_details(request, id):

    data = Product.objects.get(id=id)
    category = ProductCategory.objects.all()
    category_list = Product.objects.filter(category=data.category)[:3]
    context = {
        'data' : data,
        'category' : category,
        'category_list' : category_list
    }
    
    return render(request, 'product_template/detail.html', context)

''' Category wise sorting and implementation of filters  '''
def product_categories(request, category):
    
    selected_brand = request.GET.getlist('brandSelections')
    selected_color = request.GET.getlist('colorSelections')
    selected_range = request.GET.get('rangeSelections')

    # Logic to filter the items
    if selected_brand != [] or selected_color != []:
        if selected_color == []:
            product_data = Product.objects.filter(Q(category=category) & Q(brand__in=selected_brand))
        elif selected_brand == []:
            product_data = Product.objects.filter(Q(category=category) & Q(color__in=selected_color))
        else:
            product_data = product_data = Product.objects.filter(category=category, brand__in=selected_brand, color__in=selected_color)
    else:
        product_data = Product.objects.filter(category=category)

    # Implementing price range of products
    if selected_range:
        product_data=product_data.filter(price__lte=selected_range)

    p = Paginator(product_data, 1)
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    url = ''
    if selected_brand:
        for x in range(len(selected_brand)):
            if x==0:
                url += f"brandSelections={selected_brand[x]}"
            else:
                url += f"&brandSelections={selected_brand[x]}"

    if selected_color:
        for x in range(len(selected_color)):
            if not selected_brand and x==0:
                url += f"colorSelections={selected_color[x]}"
            else:
                url += f"&colorSelections={selected_color[x]}"
    if selected_range:
        if selected_range or selected_color:
            url += f"&rangeSelections={selected_range}"
        else:
            url += f"rangeSelections={selected_range}"

    context = {
        'product_data' : page_obj,
        'category' : ProductCategory.objects.all(),
        'brands' : Brand.objects.filter(category=category),
        'colors' : Color.objects.all(),
        'url' : url
    }
    
    return render(request, 'product_template/category.html', context)



''' Rendering wishlisted data '''
@login_required(login_url='/register')
def wishlist(request,id):
    data = Wishlist.objects.filter(user=User.objects.get(username=id))
    category_data = ProductCategory.objects.all()
    context = {
        'data':data,
        'category' : category_data
    }
    return render(request, 'product_template/customer-wishlist.html', context)

''' Functionality to add items to wishlist'''
@login_required(login_url='/register')
def addWishlist(request, uname, id):
    
    item = Wishlist.objects.filter(user=User.objects.get(id=request.user.id)).filter(product=Product.objects.get(id=id))
    if item:
        messages.error(request, "Item is already available in wishlist")
    else:
        Wishlist.objects.create(user=request.user, product=Product.objects.get(id=id), date=datetime.datetime.now)
    return redirect(f"/wishlist/{request.user}")

''' Functionality to remove items from the wishlist '''
def removeWishlist(request, uname, id):
    Wishlist.objects.get(id=id).delete()
    return redirect(f"/wishlist/{request.user}")


def addProduct(request, uname, id=None):

    if request.method == 'GET':
        if id==None:
            return render(request, 'admin_template/addProduct.html')
        else:
            return render(request, 'admin_template/addProduct.html', {'product_data' : Product.objects.get(id=id)})


    if request.method == 'POST':

        product_data={
            'product_name' : request.POST.get('product_name'),
            'product_desc' : request.POST.get('product_desc'),
            'category' : request.POST.get('product_category'),
            'brand' : request.POST.get('product_brand'),
            'color' : request.POST.get('product_color'),
            'mdl' : request.POST.get('product_mdl'),
            'price' : request.POST.get('product_price'),
            'user' : request.user,
            'stock_quantity' : request.POST.get('product_stock'),
            'image1' : request.FILES.get('image1'),
            'image2' : request.FILES.get('image2'),
            'image3' : request.FILES.get('image3'),
            'image4' : request.FILES.get('image4'),
            'image5' : request.FILES.get('image5'),
        }

        a, status = ProductCategory.objects.get_or_create(category=product_data['category'])
        product_data['category']=a
        a, status = Brand.objects.get_or_create(brand_name=product_data['brand'], category=product_data['category'])
        product_data['brand']=a
        a, status = Color.objects.get_or_create(color_name=product_data['color'])
        product_data['color']=a
        a, status = Mdl.objects.get_or_create(mdl=product_data['mdl'])
        product_data['mdl']=a
        if not id:
            Product.objects.create(**product_data)
        else:
            Product.objects.filter(id=id).update(**product_data)

        return render(request, 'admin_template/addProduct.html')
    
def delete_product(request, uname, id):
    data = Product.objects.filter(id=id, user=request.user)
    if data:
        data.delete()
    return redirect('/seller-inventory')

def sellerInventory(request):

    product_data = Product.objects.filter(user=request.user)

    return render(request, 'admin_template/inventory.html',{'product_data' : product_data})