from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from product.models import Product, ProductCategory
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
    ''' Handling POST request for registering data of user '''
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
            
            # Rendering specific pages for sellers
            if user_type == 'seller':
                return render(request, 'admin_template/signup.html')
    return render(request, 'users_template/register.html', {'catagory': ProductCategory.objects.all()})

''' Code to login User '''

def login_user(request):

    # Handleing POST request for login users.
    if request.method == 'POST':
       
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            messages.success(request, "Login Successful")
            if user.user_type == 'seller':
                return redirect(f"/admin-panel/dashboard")
            elif user.user_type == 'customer':
                return redirect('/')
        else:
            messages.error(request, "Data insufficient or Credentitials not matched")
            return redirect('/register')    
    

''' Functionality of update or render user profile data through GET or POST request '''

@login_required(login_url='/register')
def account(request, id):

    # Block to define funtionality of rendering user data
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
            context['category'] = ProductCategory.objects.all()
            return render(request, 'users_template/customer-account.html', context)
            
    
    # Block to implement functionality of updating profile data of users
    if request.method == 'POST':
        
        # Taking inputs for updated data
        updated_user = {
            'first_name' : request.POST.get('first_name'),
            'last_name' : request.POST.get('last_name'),
            'mobile' : request.POST.get('mobile'),
            'email' : request.POST.get('email')
        }
        # taking input of updated data of addresses of users
        updated_address = {
            'house' : request.POST.get('house'),
            'area' : request.POST.get('area'),
            'landmark' : request.POST.get('landmark'),
            'zip' : request.POST.get('zip'),
            'state' : request.POST.get('state'),
            'city' : request.POST.get('city'),
            'primary' : True
        }

        # Checking whether address of specific user exists or not.
        if Address.objects.filter(Q(user=request.user) & Q(primary=True)).exists():
            Address.objects.filter(Q(user=request.user) & Q(primary=True)).update(**updated_address)
        else:
            # if not then create a new address 
            updated_address['user'] = User.objects.get(id=request.user.id)
            Address.objects.create(**updated_address)
            
        User.objects.filter(id = request.user.id).update(**updated_user)
        messages.success(request, "Address updated successfully")
        if request.user.user_type == 'seller':
            return redirect(f"/adminProfile/{request.user}")
        elif request.user.user_type == 'customer':
            return redirect(f"/account/{request.user}")
    

''' Implementation of functionality of update password. '''

@login_required(login_url='/register')
def update_password(request, id):
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        cnf_password = request.POST.get('cnf_password')

        user = authenticate(username=id, password=old_password)

        if user is not None:
            if new_password == cnf_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password Updated Successfully")
                login(request, user)
                HttpResponseRedirect(request.path_info)
            else:
                messages.error(request, "Password and Confirm Password Doesn't match")
                HttpResponseRedirect(request.path_info)


# functionality of logout

@login_required(login_url='/register')
def logout_user(request, id):
    if request.user.user_type == 'seller':
        logout(request)
        return redirect('/adminlogin')
    else:
        logout(request)
        return redirect('/')


''' Implementing functionality of Admin panel '''


def admin_login(request):
    
    return render(request, 'admin_template/signin.html')

def admin_register(request):
    
    return render(request, 'admin_template/signup.html')    
    