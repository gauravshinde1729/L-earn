from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from learn_platform.models import UserProfile
from tutor.models import TutorApplicationRequest
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        messages.info(request,'You are already logged in')
        student = UserProfile.objects.filter(user=request.user)

        if not student:
            return redirect('/tutor/home')
        else:
            return redirect('/platform')
    return render(request,'home/homepage.html')

def loginPage(request):
    if request.user.is_authenticated:
        print('already authenticated')
        messages.info(request, 'You are already logged in')
        student = UserProfile.objects.filter(user=request.user)

        if not student:
            return redirect('/tutor/home')
        else:
            return redirect('/platform')
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        student = UserProfile.objects.filter(user=user)

        if user is not None:
            print('valid user')
            if not student:
                print('not a student')
                messages.error(request, "Sorry, You are not a Student . Please enter correct credentials")
                return redirect('/')
            login(request,user)
            return redirect('/platform')
        else:
            messages.info(request,'Username or Password is incorrect')

    return render(request,'home/login.html')

def registerPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        student = UserProfile.objects.filter(user=request.user)

        if not student:
            return redirect('/tutor/home')
        else:
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

def tutorApplication(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        student = UserProfile.objects.filter(user=request.user)

        if not student:
            return redirect('/tutor/home')
        else:
            return redirect('/platform')
    if(request.method=="POST"):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city = request.POST['city']
        details = request.POST['details']
        phonenumber = request.POST['phone']
        email = request.POST['email']
        experience = request.POST['experience']

        if (request.POST['firstname']=="" or request.POST['lastname']=="" or request.POST['email']=="" or request.POST['phone']==""):
            messages.warning(request,'Please Dont Leave Any Field Blank')

            return render(request, 'home/tutorApplication.html')

        new_request = TutorApplicationRequest(firstname=firstname,lastname=lastname,email=email,
                                        phonenumber=phonenumber,details=details,city=city,experience=experience)
        new_request.save()
        messages.success(request," Thank you "+firstname+" for applying as a Tutor . Your request for becoming a Tutor has been successfully submitted. Please wait until we contact you ")
        return redirect('/')


    return render(request,'home/tutorApplication.html')


