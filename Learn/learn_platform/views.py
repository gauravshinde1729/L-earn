from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from Learn.decorators import allowed_users
#if user is authunticated

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def index(request):
    return render(request,'platform/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def profilePage(request):
    user = request.user;
    profile = UserProfile.objects.get(user=user)
    context = {'profile':profile,}
    return render(request,'platform/profilepage.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def profileEdit(request):
    user = request.user;
    profile = UserProfile.objects.get(user=user)
    context = {'profile': profile, }
    if(request.method=="POST"):
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        city      = request.POST['city']
        country   = request.POST['country']
        bio       = request.POST['bio']
        profile.firstname = firstname
        profile.lastname =lastname
        profile.bio  = bio
        profile.city = city
        profile.country = country
        profile.save()
        return redirect('profilePage')

    return render(request,'platform/profileEdit.html',context)

def logoutPage(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    return redirect('/')
