from django.shortcuts import render, HttpResponse, redirect
from .models import channel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.name.lower() or query in item.category.lower() :
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    product = channel.objects.all()
    prod = [item for item in product if searchMatch(query, item)]
    n = len(prod)
    params = {'product': prod, 'n': n}
    return render(request, 'user/search.html', params)


def store(request, cat):
    product=channel.objects.filter(category=cat)
    n=len(product)
    params = {'product': product[::-1], 'n': n}
    return render(request, 'user/store.html', params)

def storeinfo(request, myid):
    prod = channel.objects.all()
    product=channel.objects.filter(id=myid)
    return render(request, 'user/storeinfo.html', {'product':product[0], 'prod': prod})

def Login(request):
    return render(request, 'user/Login.html')

def signup(request):
    return render(request, 'user/registration.html')

def business(request):
    return render(request, 'user/business.html')

def prod(request):
    color = {'color1':'black'}
    return render(request, 'user/prodview.html', color)

def product(request):
    return render(request, 'user/addproduct.html')

def cart(request):
    return render(request, 'user/cart.html')

def handleSignup(request):
    if request.method == 'POST':

        # Get user params
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Checks for erroneous inputs

        #Username lenght check
        if len(username) > 10:
            messages.error(request, 'Username too long')
            return redirect('home')

        #Alphanumeric check
        if not username.isalnum():
            messages.error(request, 'Username must comprise of alphanumeric characters')
            return redirect('home')

        #Password match check
        if password != cpassword:
            messages.success(request, 'Passwords do not match.')
            return redirect('home')

        #Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.name = username
        myuser.email = email
        myuser.password = password
        myuser.save()
        messages.success(request, 'Your Account has been created')
        return redirect('home')

    return HttpResponse('404 - NOT FOUND')


def handleLogin(request):
    if request.method == 'POST':

        # Get user params
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username= loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials. Please try again.")
            return redirect('home')

    return HttpResponse('404 - NOT FOUND')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')