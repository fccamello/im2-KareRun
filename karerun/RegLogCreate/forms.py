from django import forms
from .models import User,Event
from datetime import date, timedelta

class RegisterUserForm(forms.ModelForm):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    

    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': '1900-01-01', 'max': date.today().isoformat()})
    )
    
    sex = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)

    
    class Meta:
        model = User
        fields = ['firstname','lastname','username','email','password','birthdate','sex']
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
    # eventcategory = forms.CharField(widget=forms.Textarea)
    eventcategory = forms.CharField(max_length=100)
    eventlocation = forms.CharField(max_length=100)
    eventdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': (date.today() + timedelta(days=1)).isoformat()})
    )

    closedate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': (date.today() + timedelta(days=1)).isoformat()})
    )

    eventtime = forms.TimeField(widget = forms.TimeInput(attrs={'type':'time'}))
    # inclusions = forms.CharField(widget=forms.Textarea)
    # inclusions = forms.CharField(widget=forms.HiddenInput())
    inclusions = forms.JSONField()  # Use a JSONField for inclusions
    bannerimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    inclusionimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    sizechartimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    racerouteimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    maxSlots = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))
    class Meta:
        model = Event
        fields = ['eventname','eventdetails','eventcategory','eventlocation','eventdate','eventtime','inclusions','bannerimage','inclusionimage','sizechartimage','racerouteimage','maxSlots', 'closedate']
    