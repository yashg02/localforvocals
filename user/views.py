from django.shortcuts import render
from django.http import HttpResponse
from .models import channel


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
    return render(request, 'user/store.html', params)


def store(request, cat):
    product=channel.objects.filter(category=cat)
    params = {'product': product[::-1]}
    return render(request, 'user/store.html', params)

def storeinfo(request, myid):
    prod = channel.objects.all()
    product=channel.objects.filter(id=myid)
    return render(request, 'user/storeinfo.html', {'product':product[0], 'prod': prod})

def login(request):
    return render(request, 'user/login.html')

def signup(request):
    return render(request, 'user/registration.html')

def business(request):
    return render(request, 'user/business.html')

def prod(request):
    return render(request, 'user/prodview.html') 
