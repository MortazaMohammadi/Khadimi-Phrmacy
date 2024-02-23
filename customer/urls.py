from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('customer_view' , customer_view , name="customer_view"),
    path('add_customer_view' , add_customer_view , name="add_customer_view"),
    path('update_customer_view/<int:cid>',update_customer_view,name="update_customer_view"),
    path('delete_customer/<int:cid>',delete_customer,name="delete_customer"),
    path('loen_view' , loen_view , name="loen_view"),
    path('add_loen_view' , add_loen_view , name="add_loen_view"),
    path('update_loen_view/<int:lid>',update_loen_view,name="update_loen_view"),
    path('delete_loen/<int:lid>',delete_loen,name="delete_loen"),
]