from django.shortcuts import render,redirect
from django.urls import path
from .models import User
from .forms import RegisterUserForm
<<<<<<< HEAD
from datetime import date
=======
>>>>>>> 2ab8c514eddc9bd5460e8aec00c4ad87f4a0a07b
# Create your views here.
def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User()
            user.firstname = form.cleaned_data['firstname']
            user.lastname = form.cleaned_data['lastname']
<<<<<<< HEAD
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
=======
            user.birthdate = form.cleaned_data['birthdate']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('register')
    else:
        form = RegisterUserForm()
    return render(request,'RegLogCreate/register.html',{'forms':form})
>>>>>>> 2ab8c514eddc9bd5460e8aec00c4ad87f4a0a07b
