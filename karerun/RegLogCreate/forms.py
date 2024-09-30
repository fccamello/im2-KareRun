from django import forms
from .models import User

class RegisterUserForm(forms.ModelForm):
    birthdate = forms.DateField(widget = forms.SelectDateWidget())
    class Meta:
        model = User
        fields = ['firstname','lastname','username','email','password']
        widgets = {
            'password':forms.PasswordInput,
            'email':forms.EmailInput
        }