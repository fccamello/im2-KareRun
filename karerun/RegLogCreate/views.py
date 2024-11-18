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
    if request.method == 'POST':
        print("received POST for register")
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            print("saved user")
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = RegisterUserForm()
    return render(request,'register.html',{'forms':form})

def logout(request):
    del request.session['userID']
    return redirect('index')

def login(request):
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
                return redirect('index')
            else:
                print("error/wrong password")
                return redirect('login')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request,'login.html',{'forms':form})

def createEvent(request):
    userId = request.session.get('userID',None)
    userName = None
    if userId is not None:
        userName = User.objects.get(userid = userId).username
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
            form.save()
            print("saved event")
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = CreateEvent()
    context['forms'] = form
    return render(request, 'createEvent.html', context)