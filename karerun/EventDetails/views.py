import logging
from django.shortcuts import render, get_object_or_404
from RegLogCreate.models import Event 

def event_detail(request, event_id):
    event = get_object_or_404(Event, eventid=event_id) 
    print("Banner Image URL:", event.bannerimage.url) 
    return render(request, 'event_details.html', {'event': event}) 
