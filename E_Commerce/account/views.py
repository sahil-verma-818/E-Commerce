from django.shortcuts import render, redirect
from product.models import Product, product_category
from .models import User,Address
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.conf import settings



# Create your views here.

'''
    Code to register user (Whether Customer or Seller).
'''

def register(request):
    category_data = product_category.objects.all()

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname', " ")
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user-type')

        # Checking if User with perticular email exists or not
        if User.objects.filter(email=email).exists():
            messages.error(request, "An Existing user already available with this gmail. Try another one.")
        else:
            username = email.split('@')[0]
            User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password, user_type=user_type)
            messages.success(request, f"User Successfully Created with username : {username}")
            if user_type == 'seller':
                return render(request, 'admin_template/signup.html')
    return render(request, 'users_template/register.html', {'category': category_data})

''' Code to login User '''

def login_user(request):
    if request.method == 'POST':
       
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            if user.user_type == 'seller':
                return redirect(f"/admin-panel/dashboard")
            elif user.user_type == 'customer':
                return redirect('/')
        else:
            messages.error(request, "Data insufficient or Credentitials not matched")
            return redirect('/register')    
    


@login_required(login_url='/register')
def account(request, id):
    if request.method == 'GET':
        try:
            data1 = User.objects.get(id=request.user.id)
            data2 = Address.objects.get(Q(user=request.user) & Q(primary=True))
        except User.DoesNotExist:
            data1 = None
        except Address.DoesNotExist:
            data2 = None

        context = {
            'data1' : data1,
            'data2' : data2,
        }

        if request.user.user_type == 'seller':
            return render(request, 'admin_template/profile.html', context)
        elif request.user.user_type == 'customer':
            context['category'] = product_category.objects.all()
            return render(request, 'users_template/customer-account.html', context)
            
    
    if request.method == 'POST':
            
        updated_user = {
            'first_name' : request.POST.get('first_name'),
            'last_name' : request.POST.get('last_name'),
            'mobile' : request.POST.get('mobile'),
            'email' : request.POST.get('email')
        }

        updated_address = {
            'house' : request.POST.get('house'),
            'area' : request.POST.get('area'),
            'landmark' : request.POST.get('landmark'),
            'zip' : request.POST.get('zip'),
            'state' : request.POST.get('state'),
            'city' : request.POST.get('city'),
            'primary' : True
        }
        if Address.objects.filter(user=request.user).exists() == False:
            updated_address['user'] = User.objects.get(id=request.user.id)
            Address.objects.filter(user=request.user).update_or_create(**updated_address)
        else:
            Address.objects.filter(user=request.user).update(**updated_address)
        User.objects.filter(id = request.user.id).update(**updated_user)
        if request.user.user_type == 'seller':
            return redirect(f"/adminProfile/{request.user}")
        elif request.user.user_type == 'customer':
            return redirect(f"/account/{request.user}")
    


@login_required(login_url='/register')
def update_password(request, id):
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        cnf_password = request.POST.get('cnf_password')

        user = authenticate(username=id, password=old_password)
        print(user)

        if user is not None:
            if new_password == cnf_password:
                user.set_password(new_password)
                user.save()
    return redirect(f"/account/{user.username}")



@login_required(login_url='/register')
def logout_user(request, id):
    if request.user.user_type == 'seller':
        logout(request)
        return redirect('/adminlogin')
    else:
        logout(request)
        return redirect('/')

@login_required(login_url='/adminlogin')
def adminHome(request):

    return render(request, 'admin_template/index.html')

def adminLogin(request):
    
    return render(request, 'admin_template/signin.html')

def adminRegister(request):
    
    return render(request, 'admin_template/signup.html')    
    