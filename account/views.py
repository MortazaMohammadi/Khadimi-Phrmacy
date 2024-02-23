from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from khademi_pharmacy.urls import *
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        muser = User.objects.get(username = user)
        print (muser.first_name)
        return redirect('/dashborad')
        
    else:   
        context = {
            }
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashborad')
            else:
                context['error_message'] = 'Invalid username or password'
        return render(request , 'account/login.html' ,context)

def register_user(request):
    context = {

        }
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        
        if password != repassword:
            context['errors_password'] = 'password mismatch'
        elif User.objects.filter(email=email).exists():
            context['errors_email'] = 'email already exists'
        elif User.objects.filter(username=user_name).exists():
            context['errors_email'] = 'username already exists'
        else:
            user = User.objects.create_user(username=user_name , email = email , password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('/dashborad')
    return render(request, 'account/register.html' , context)

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def calendar_view(request):
    return render(request , 'calendar/calendar.html')

@login_required(login_url='/')
def user_profile_view(request):
    return render(request , 'userProfile/user_profile.html')