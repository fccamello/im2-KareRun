from django.shortcuts import render,redirect
from django.urls import path
from django.contrib.auth import login as user_login
from .models import User
from .forms import RegisterUserForm,LoginForm,CreateEvent
from datetime import date
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.
def register(request):
    user = User.objects.all()
    errors = None
    if request.method == 'POST':
        print("received POST for register")
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            print("saved user")
            return redirect('login')
        else:
            print("Erorr Found:")
            errors = form.errors
    else:
        form = RegisterUserForm()
    print(errors)
    return render(request,'register.html',{'forms':form,'errors':errors})

def logout(request):
    del request.session['userID']
    return redirect('index')

def login(request):
    context = {
        'forms':None,
        'errors':None
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.login(email,password)
            print(user)
            if user is not None:
                request.session['userID'] = user.userid
                print("success")
                context['user'] = user
                context['userId'] = user.userid
                return redirect('homepage')
            else:
                form = LoginForm()
                print("error/wrong password")
                context['forms'] = form
                context['errors'] = "Invalid email or password"
                return render(request,'login.html',context) 
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request,'login.html',{'forms':form})

def createEvent(request):
    userId = request.session.get('userID',None)
    userName = None
    if userId is not None:
        user = User.objects.get(userid = userId)
        userName = user.username
        if user.isEventOrganizer == False:
            return redirect('index')
        print(userId)
    else:
        print("no session")

    context ={
        'userName':userName
    }
    if request.method == 'POST':
        print("received event POST")
        form = CreateEvent(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.organizerId = userId
            user.save()
            print("saved event")
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = CreateEvent()
    context['forms'] = form
    return render(request, 'createEvent.html', context)