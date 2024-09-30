from django import forms
from .models import User

class RegisterUserForm(forms.ModelForm):
    birthdate = forms.DateField(widget = forms.DateInput(attrs={'type':'date','min':'1900-01-01'}))
    class Meta:
        model = User
        fields = ['firstname','lastname','username','email','password','birthdate']
        widgets = {
            'password':forms.PasswordInput,
            'email':forms.EmailInput
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password']