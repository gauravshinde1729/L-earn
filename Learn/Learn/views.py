from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from learn_platform.models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        messages.info(request,'You are already logged in')
        return redirect('/platform')
    return render(request,'home/homepage.html')

def loginPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('/platform')
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/platform')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,'home/login.html')

def registerPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('/platform')
    form = CreateUserForm()

    if(request.method=="POST"):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                messages.success(request, 'You have been successfully registered as ' + username)
                login(request, user)
                user_profile = UserProfile(user=user)
                user_profile.save()
                return redirect('/platform')
            else:
                messages.error(request,"We couldn't register you. Please try again ")
    context = {'form':form}
    return render(request,'home/register.html',context)

