from django.shortcuts import render
from product.models import Product

# Create your views here.

def home(request):
    context = {}
    a = 0
    for x in Product.objects.all().values():
        context[a] = {
            'category' : x['category'],
            'price' : x['price']
        }
        a+=1
    
    return render(request, 'product_template/index.html', context=context)

def register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_email = request.POST.get('login_email')
        login_password = request.POST.get('login_password')

        print(name)
        print(email)
        print(password)
        print(login_email)
        print(login_password)


    if id == 'kanha@123':
        print('Kanha is being executed.')
        return render(request, 'users_template/register.html')
    return render(request, 'users_template/register.html')
    


def account(request, id):
    if id == 'kanha@123':
        print('Kanha is being executed.')
        return render(request, 'users_template/register.html')
    return render(request, 'users_template/customer-account.html')