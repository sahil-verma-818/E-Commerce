from django.shortcuts import render, redirect
from product.models import Product
from .models import User,Address
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    
    data = Product.objects.all()
    context = {
        'data' : data
    }
    
    return render(request, 'product_template/index.html', context=context)

def register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        

        if User.objects.filter(email=email).exists():
            print("Data already present.")
        else:
            username = email.split('@')[0]
            name = name.split(' ', 1)
            User.objects.create_user(username=username, first_name=name[0], last_name=name[1], email=email, password=password)

    return render(request, 'users_template/register.html')

def login_user(request):
    if request.method == 'POST':
       
        username = request.POST.get('login-email')
        password = request.POST.get('login-password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            
            return redirect(f"account/{user.username}")

    return render(request, 'users_template/register.html')
    

@login_required(login_url='/register')
def account(request, id):
    if request.method == 'GET':
        try:
            data1 = User.objects.get(username = id)
            data2 = Address.objects.get(user=data1)
            
        except User.DoesNotExist:
            data = None

        context = {
            'data1' : data1,
            'data2' : data2
        }

        return render(request, 'users_template/customer-account.html', context)
    
    if request.method == 'POST':

        data1 = User.objects.get(username = id)
        data2 = Address.objects.get(user=data1)
        

        first_name = request.POST.get('first_name', data1.first_name)
        last_name = request.POST.get('last_name')
        house = request.POST.get('house')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        

        return render(request, 'users_template/customer-account.html')