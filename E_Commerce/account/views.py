
# Imports
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,JsonResponse
from product.models import Product, ProductCategory
from .models import User,Address
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
# ===========================================================================-------------- #


# Create your views here.


# ******************** Code to register user *****************************
def register(request):

    # ===================================================================
    ''' Handling POST request for registering data of user '''
    if request.method == 'POST':

        #================================================================
        # Fetching all the inputs
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('usertype')

        # ===============================================================
        # Checking if User with perticular email exists or not
        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error','message' : 'An Existing user already available with this email. Try another one.'})
        else:
            username = email.split('@')[0]
            User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password, user_type=user_type)
            return JsonResponse({'status' : 'success' , 'message' : f"New user created with username {username}" , 'redirect' : '/adminlogin'})
        # ==================================================================================  
    # Rendering specific pages for sellers
    return render(request, 'users_template/register.html', {'catagory': ProductCategory.objects.all()})

# ===============================================================================================


# ************************ Code to login user *****************************
def login_user(request):

    # Handleing POST request for login users.
    if request.method == 'POST':
       
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')
        user = authenticate(username=username, password=password)

        #==============================================================

        if user is not None:
            login(request, user=user)

            # ==========================================================
            if user.user_type == 'seller':
                return JsonResponse({'status':'success', 'message':'Login Successful', 'redirect' : '/admin-panel/dashboard'})
            elif user.user_type == 'customer':
                return JsonResponse({'status':'success', 'message':'Login Successful', 'redirect' : '/'})
            # ============================================================
        else:
            return JsonResponse({'status':'error', 'message':'Credentials not matched to any data.'})
        
        # =================================================================
    
#================================================================================================


# ===============================================================================================

''' Functionality of update or render user profile data through GET or POST request '''
@login_required(login_url='/register')
def account(request, id):

    # ======================================================

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

        # =======================================================================

        if request.user.user_type == 'seller':
            return render(request, 'admin_template/profile.html', context)
        elif request.user.user_type == 'customer':
            context['category'] = ProductCategory.objects.all()
            return render(request, 'users_template/customer-account.html', context)
            
        # =======================================================================

    # Block to implement functionality of updating profile data of users
    if request.method == 'POST':

        # Update profile picture
        profile_pic = request.FILES.get('profile_pic')
        if profile_pic:
            user=User.objects.get(id=request.user.id)
            user.profile_pic=profile_pic
            user.save()
            return JsonResponse({'status':'success', 'message': 'Profile Picture updated successfully'})
        
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
        return JsonResponse({'status':'success', 'message':'Personal Details updated successfully'})

    

''' Implementation of functionality of update password. '''

@login_required(login_url='/register')
def update_password(request, id):
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        cnf_password = request.POST.get('cnf_password')

        user = authenticate(username=id, password=old_password)

        if user:
            if new_password == cnf_password:
                user.set_password(new_password)
                user.save()
                login(request, user)
                return JsonResponse({'status':'success', 'message':'Password Updated Successfully'})
            else:
                return JsonResponse({'status':'message', 'message': 'Password and confirm password does not match'})
            
        else:
            return JsonResponse({'status':'error', 'message':'Wrong password!! Try Again'})


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
    