from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search, name="search"),
    path('store/<str:cat>', views.store, name="store"),
    path("storeinfo/<str:myname>", views.storeinfo, name="ProductView"),
    path('plogin/', views.plogin, name='plogin'),
    path('blogin/', views.blogin, name='blogin'),
    path('handleSignup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('signup/', views.signup, name='signup'),
    path('business/', views.business, name='business'),
    path('prodview/', views.prod, name="ProductView"),
    path('product/', views.product, name="Product"),
    path('cart/', views.cart, name="Cart"),
    path('addprod/', views.addprod, name="AddProduct"),
    path('signin/', views.signin, name="SignIN")
    
]