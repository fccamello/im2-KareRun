from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'cover_photo']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
