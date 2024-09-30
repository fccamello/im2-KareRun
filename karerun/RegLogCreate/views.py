from django.shortcuts import render,redirect
from django.urls import path
from .models import User
from .forms import RegisterUserForm,LoginForm
from datetime import date
from django.contrib.auth import authenticate
# Create your views here.
def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved user")
            return redirect('sucess')
    else:
        form = RegisterUserForm()
    return render(request,'RegLogCreate/register.html',{'forms':form})

def success(request):
    return render(request,'RegLogCreate/sucess.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('success')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request,'RegLogCreate/login.html',{'forms':form})