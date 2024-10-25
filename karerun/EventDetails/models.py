from django.shortcuts import render
from RegLogCreate.models import Event

def event_detail_view(request, event_id):
    event = Event.objects.get(eventid=event_id)
    return render(request, 'event_details.html', {'event': event})
