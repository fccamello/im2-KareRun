from django.shortcuts import render,redirect
from django.urls import path
from .models import User
from .forms import RegisterUserForm
# Create your views here.
def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User()
            user.firstname = form.cleaned_data['firstname']
            user.lastname = form.cleaned_data['lastname']
            user.birthdate = form.cleaned_data['birthdate']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('register')
    else:
        form = RegisterUserForm()
    return render(request,'RegLogCreate/register.html',{'forms':form})
