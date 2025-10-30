from datetime import datetime
from django.urls import re_path, path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from capstone.app import forms, views  # 👈 key fix

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),

    re_path(r'^$', views.index, name='index'),
    re_path(r'^special/', views.special, name='special'),

    # updated include path
    re_path('', include(('capstone.app.urls', 'app'), namespace='app')),

    re_path(r'^logout/$', views.user_logout, name='logout'),

    path('foodie/', views.foodie, name='foodie'),
    path('yelping/', views.yelping, name='yelping'),
    path('home/yelping/', views.yelping, name='yelping'),
    path('googling/', views.googling, name='googling'),
    path('home/googling/', views.googling, name='googling'),
    path('nutritioning/', views.nutritioning, name='nutritioning'),
    path('home/nutritioning/', views.nutritioning, name='nutritioning'),
    path('foodmacros/', views.foodmacros, name='foodmacros'),
    path('home/foodmacros/', views.foodmacros, name='foodmacros'),
]
