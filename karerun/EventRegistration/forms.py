from django import forms

from .models import Registration

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30,  required=False)
    last_name = forms.CharField(max_length=30)
    AGE_CHOICES = [
        ('20 and below', '20 and below'),
        ('21 to 30', '21 to 30'),
        ('31 to 40', '31 to 40'),
        ('41 to 50', '41 to 50'),
        ('51 and above', '51 and above'),
    ]
    
    age_category = forms.ChoiceField(choices=AGE_CHOICES, widget=forms.RadioSelect)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    contact_number = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=20)
    emergency_number = forms.CharField(max_length=15)
    category_ni = forms.CharField(widget=forms.HiddenInput(), max_length=30) 
    category_price = forms.CharField(widget=forms.HiddenInput()) 
    singlet_size = forms.CharField(max_length=50, required=False)
    finisher_shirt_size = forms.CharField(max_length=50, required=False)

    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories', None)
        super().__init__(*args, **kwargs)
        
        if categories:
            self.fields['category_ni'].choices = [(cat, cat) for cat in categories]
        
        if categories:
            self.fields['category_ni'].initial = categories[0]
   
    # def clean(self):
    #     cleaned_data = super().clean()
        
    #     inclusions = {
    #         'singlet_size': cleaned_data.get('singlet_size'),
    #         'finisher_shirt_size': cleaned_data.get('finisher_shirt_size')
    #     }
        
    #     cleaned_data['inclusions'] = inclusions
    #     return cleaned_data

        