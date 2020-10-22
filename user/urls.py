from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search, name="search"),
    path('store/<str:cat>', views.store, name="store"),
    path("store/storeinfo/<int:myid>", views.storeinfo, name="ProductView"),
    path('Login/', views.Login, name='login'),
    path('handleSignup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('signup/', views.signup, name='signup'),
    path('signup/business/', views.business, name='business'),
    path('store/storeinfo/prodview/', views.prod, name="ProductView"),
    path('product/', views.product, name="Product"),
    path('cart/', views.cart, name="Cart")
]