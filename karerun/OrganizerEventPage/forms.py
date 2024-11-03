from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location']

class EventCoverPhotoForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['cover_photo']
