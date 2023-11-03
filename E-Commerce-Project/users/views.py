from django.shortcuts import render

# Create your views here.

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

    return render(request, 'users_template/register.html')


def account(request):

    return render(request, 'users_template/customer-account.html')