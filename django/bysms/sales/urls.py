#!/usr/bin/evn python
#-*- coding:utf-8 -*-


from django.urls import path 

from . import views



urlpatterns = [
    path('orders/', views.listorders),
    path('peoples/', views.people),
]