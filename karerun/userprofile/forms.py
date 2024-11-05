from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['cover_photo', 'profile_image', 'bio', 'birthdate', 'gender', 'organization']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }