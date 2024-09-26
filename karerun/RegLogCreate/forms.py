from django import forms
from .models import User

class RegisterUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['firstname','lastname','birthdate','username','email','password']
        
