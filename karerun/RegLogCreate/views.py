from django.shortcuts import render,redirect
from django.urls import path
from .models import User
from .forms import RegisterUserForm
from datetime import date
# Create your views here.
def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User()
            user.firstname = form.cleaned_data['firstname']
            user.lastname = form.cleaned_data['lastname']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            birthdate = date(int(request.POST['birthdate_year']),
                             int(request.POST['birthdate_month']),
                             int(request.POST['birthdate_day']))
            user.birthdate = birthdate
            user.save()
            print("saved user")
            return redirect('sucess')
    else:
        form = RegisterUserForm()
    return render(request,'RegLogCreate/register.html',{'forms':form})

def success(request):
    return render(request,'RegLogCreate/sucess.html')