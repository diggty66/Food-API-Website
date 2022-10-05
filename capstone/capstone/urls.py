"""
Definition of urls for capstone.
"""

from datetime import datetime
from django.urls import re_path as url, path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.forms import UserForm
from app import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^app/', include('app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('foodie/', views.foodie, name='foodie'),
    path('yelp/', views.yelp, name='yelp'),
]
