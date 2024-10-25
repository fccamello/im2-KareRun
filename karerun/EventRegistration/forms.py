from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=30, label='Middle Name', required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Middle Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}))

    AGE_CHOICES = [
        ('20 and below', '20 and below'),
        ('21 to 30', '21 to 30'),
        ('31 to 40', '31 to 40'),
        ('41 to 50', '41 to 50'),
        ('51 and above', '51 and above'),
    ]
    age = forms.ChoiceField(choices=AGE_CHOICES, label='Age', widget=forms.Select(attrs={'class': 'form-input'}))

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer not to say'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', widget=forms.RadioSelect)

    contact_number = forms.CharField(max_length=15, label='Contact Number', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Contact Number'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    emergency_number = forms.CharField(max_length=15, label='Emergency Number', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Emergency Number'}))
