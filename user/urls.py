from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search, name="search"),
    path('store/<str:cat>', views.store, name="store"),
    path("store/storeinfo/<int:myid>", views.storeinfo, name="ProductView"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/business/', views.business, name='business'),
    path('store/storeinfo/prodview/', views.prod, name="ProductView")
]