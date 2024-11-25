import json
import logging
from django.shortcuts import render, get_object_or_404
from RegLogCreate.models import Event 
from collections import defaultdict
from EventRegistration.models import Registration

def event_detail(request, event_id):
    event = get_object_or_404(Event, eventid=event_id) 
    userId = request.session.get('userID',None)
    eventname_split = event.eventname.split(' ', 1)
    first_word = eventname_split[0]
    rest_of_text = " ".join(eventname_split[1:]) if len(eventname_split) > 1 else ''

    inclusions_list = json.loads(event.inclusions) if isinstance(event.inclusions, str) else event.inclusions

    category_inclusions = {}
    category_prices = {}


    categories = event.eventcategory.split(',')
    category_list = [category.strip() for category in categories]
    
    for category in category_list:
        category_items = [
            {
                'inclusion': item['inclusion'],
                'size': item['size'],
                'price': item['price']
            }
            for item in inclusions_list 
            if item['category'].strip() == category
        ]
        category_inclusions[category] = category_items
        
        unique_inclusions = defaultdict(set)
        for category, items in category_inclusions.items():
            for item in items:
                unique_inclusions[category].add(item['inclusion'])  

        price = next((item['price'] for item in category_items if item['price']), "0")
        category_prices[category] = price

    unique_inclusions_dict = {k: list(v) for k, v in unique_inclusions.items()}

    #Get number of participants
    num_registrants = Registration.objects.filter(event = event).count()

    print("Banner Image URL:", event.bannerimage.url) 
    return render(request, 'event_details.html', {
        'userName': "this is not needed",
        'event': event,
        'userID': userId,
        'first_word': first_word,
        'rest_of_text': rest_of_text,
        'categories': category_list,
        'unique_inclusions': unique_inclusions_dict,
         'category_prices': category_prices,
        'num_registrants': num_registrants,
    })
