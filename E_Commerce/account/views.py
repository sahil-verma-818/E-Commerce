from django.shortcuts import render, redirect
from product.models import Product
from .models import User,Address
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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
            messages.error(request, "User Already Available")
        else:
            username = email.split('@')[0]
            name = name.split(' ', 1)
            User.objects.create_user(username=username, first_name=name[0], last_name=name[1], email=email, password=password)
            messages.success(request, f"User Successfully Created with username : {username}")
    return render(request, 'users_template/register.html')



def login_user(request):
    if request.method == 'POST':
       
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect(f"account/{request.user}")
        else:
            messages.error(request, "Data insufficient or Credentitials not matched")
            return redirect('/register')

    # return render(request, 'users_template/register.html')    
    


@login_required(login_url='/register')
def account(request, id):
    if request.method == 'GET':
        print(request.user.id)
        try:
            data1 = User.objects.get(id=request.user.id)
            data2 = Address.objects.get(user=request.user)
            print(data1.first_name)
        except User.DoesNotExist:
            data1 = None
        except Address.DoesNotExist:
            data2 = None

        context = {
            'data1' : data1,
            'data2' : data2
        }

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
            'city' : request.POST.get('city')
        }
        if Address.objects.filter(user=request.user).exists() == False:
            updated_address['user'] = User.objects.get(id=request.user.id)
            Address.objects.filter(user=request.user).update_or_create(**updated_address)
        else:
            Address.objects.filter(user=request.user).update(**updated_address)
        User.objects.filter(id = request.user.id).update(**updated_user)

        return render(request, 'users_template/customer-account.html')
    


@login_required
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



@login_required
def logout_user(request, id):
    logout(request)
    return redirect('/')
    