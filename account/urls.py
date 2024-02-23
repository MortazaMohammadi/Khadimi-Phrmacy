from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path('' , login_user , name='login_user'),
    path('register_user' , register_user , name='register_user'),
    path('logout_user' , logout_user , name='logout_user'),
    path('calendar_view' , calendar_view , name='calendar_view'),
    path('user_profile_view' , user_profile_view , name='user_profile_view'),
]