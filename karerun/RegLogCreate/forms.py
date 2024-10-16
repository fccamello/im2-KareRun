from django import forms
from .models import User,Event

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

class CreateEvent(forms.ModelForm):
    eventname = forms.CharField(max_length=100)
    eventdetails = forms.CharField(widget = forms.Textarea)
    eventcategory = forms.CharField(widget=forms.Textarea)
    eventlocation = forms.CharField(max_length=100)
    eventdate = forms.DateField(widget = forms.DateInput(attrs={'type':'date'}))
    eventtime = forms.TimeField(widget = forms.TimeInput(attrs={'type':'time'}))
    inclusions = forms.CharField(widget=forms.Textarea)
    bannerimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    inclusionimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    sizechartimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    racerouteimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    class Meta:
        model = Event
        fields = ['eventname','eventdetails','eventcategory','eventlocation','eventdate','eventtime','inclusions','bannerimage','inclusionimage','sizechartimage','racerouteimage']
    