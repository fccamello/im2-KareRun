import logging
from django.shortcuts import render, get_object_or_404
from RegLogCreate.models import Event 

def event_detail(request, event_id):
    event = get_object_or_404(Event, eventid=event_id) 
    eventname_split = event.eventname.split(' ', 1)
    first_word = eventname_split[0]
    rest_of_text = " ".join(eventname_split[1:]) if len(eventname_split) > 1 else ''

    
    categories = event.eventcategory
    category_list = [f"{str(x)}km "for x in categories.split(',')]

    

    print("Banner Image URL:", event.bannerimage.url) 
    return render(request, 'event_details.html', {
        'event': event,
        'first_word': first_word,
        'rest_of_text': rest_of_text,
        'categories': category_list,
    })
