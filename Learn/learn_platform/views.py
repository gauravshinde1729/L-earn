from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
#if user is authunticated

@login_required(login_url='login')
def index(request):
    return render(request,'platform/home.html')

@login_required(login_url='login')
def profilePage(request):
    user = request.user;
    profile = UserProfile.objects.get(user=user)
    context = {'profile':profile,}
    return render(request,'platform/profilepage.html',context)

def logoutPage(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    return redirect('/')
