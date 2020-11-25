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

def storeinfo(request, myname):
    prod = channel.objects.all()
    product=channel.objects.filter(name=myname)
    return render(request, 'user/storeinfo.html', {'product':product[0], 'prod': prod})

def plogin(request):
    return render(request, 'user/plogin.html')

def blogin(request):
    return render(request, 'user/blogin.html')

def signin(request):
    return render(request, 'user/signin.html')

def signup(request):
    return render(request, 'user/private.html')

def business(request):
    return render(request, 'user/business.html')

def prod(request):
    color = {'color1':'black'}
    return render(request, 'user/prodview.html', color)

def product(request):
    return render(request, 'user/addproduct.html')

def cart(request):
    return render(request, 'user/cart.html')


## USER Login, Logout, SignUp

def handleSignup(request):
    if request.method == 'POST':

        # Get user params
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Checks for erroneous inputs

        #Username length check
        if len(username) > 10:
            messages.error(request, "Username too long")
            return redirect('home')

        #Alphanumeric check
        if not username.isalnum():
            messages.error(request, "Username must comprise of alphanumeric characters")
            return redirect('home')

        #Password match check
        if password != cpassword:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

        #Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.name = username
        myuser.email = email
        myuser.set_password = password
        myuser.save()
        messages.success(request, "Your Account has been created")
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


## BUISNESS Login, Logout, SignUp

def BSignup(request):
    if request.method == 'POST':

        # Get user params
        storename = request.POST['storename']
        shopemail = request.POST['shopemail']
        shop_pass = request.POST['shop_pass']
        shop_pass1 = request.POST['shop_pass1']

        #Checks for erroneous inputs

        #Storename length check
        if len(storename) > 10:
            messages.error(request, "Storename too long")
            return redirect('home')

        #Alphanumeric check
        if not storename.isalnum():
            messages.error(request, "Storename must comprise of alphanumeric characters")
            return redirect('home')

        #Password match check
        if shop_pass != shop_pass1:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

        #Create User
        Buser = User.objects.create_user(storename, shopemail, shop_pass)
        Buser.name = storename
        Buser.email = shopemail
        Buser.set_password = shop_pass
        Buser.is_staff = True
        Buser.save()
        messages.success(request, "Your Account has been created")
        return redirect('home')

    return HttpResponse('404 - NOT FOUND')

def BLogin(request):
    if request.method == 'POST':

        # Get user params
        shop_email = request.POST['shop_email']
        shop_pass3 = request.POST['shop_pass3']

        user = authenticate(username= shop_email, password= shop_pass3)

        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect('home')

            else:
                messages.error(request, "Login using a business account.")
                return redirect('home')
            
        else:
            messages.error(request, "Invalid Credentials. Please try again.")
            return redirect('home')

    return HttpResponse('404 - NOT FOUND')

def BLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')



## Add Product
def addprod(request):
    if request.method == 'POST':
        name = request.POST.get('storename', '')
        category = request.POST.get('category', '')
        desc = request.POST.get('desc', '')
        image = request.POST.get('image', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('shopemail', '')
        password = request.POST.get('shop_pass', '')
        Channel = channel(name=name, category=category, desc=desc, image=image, phone=phone,
                          email=email, password=password)
        Channel.save()
        messages.success(request, "Your Store has been created")
        return redirect('home')

    return HttpResponse('404 - NOT FOUND')

def checkout(request):
    return render(request, 'user/checkout.html')
