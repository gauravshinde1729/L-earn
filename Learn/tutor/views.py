from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import TutorProfile
from Learn.decorators import allowed_users
# Create your views here.

def tutorLogin(request):
    if request.user.is_authenticated:
        tutor = TutorProfile.objects.filter(user=request.user)
        if not tutor:
            return redirect('/platform')
        else:
            return redirect('/tutor/home')


    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']

        user =authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Sorry , We couldn't log you in as a tutor . Please enter correct username and password")
            return redirect('/tutor')

        tutor = TutorProfile.objects.filter(user=user)
        if not tutor:
            messages.error(request,"Sorry , We couldn't log you in as a tutor . Please enter correct username and password")
            return redirect('/tutor')

        login(request,user)
        return redirect('home/')
    return render(request,'tutor/tutorlogin.html')

@login_required(login_url='/tutor')
@allowed_users(allowed_roles=['tutor'])
def tutorHome(request):
    return render(request,'tutor/tutorhome.html')