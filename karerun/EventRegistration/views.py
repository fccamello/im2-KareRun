from collections import defaultdict
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegistrationForm
from RegLogCreate.models import Event
import json

def event_reg(request, event_id):
    event = get_object_or_404(Event, eventid=event_id)
    
    eventname_split = event.eventname.split(' ', 1)
    first_word = eventname_split[0]
    rest_of_text = eventname_split[1] if len(eventname_split) > 1 else ''
    
    # Parse categories
    categories = event.eventcategory.split(',')
    category_list = [category.strip() for category in categories]
    
    # Parse inclusions
    inclusions_list = json.loads(event.inclusions) if isinstance(event.inclusions, str) else event.inclusions
    
    # Create category_inclusions dictionary with full inclusion data and prices
    category_inclusions = {}
    category_prices = {}
    
    for category in category_list:
        # Get all inclusions for this category
        category_items = [
            {
                'inclusion': item['inclusion'],
                'size': item['size'],
                'price': item['price']
            }
            for item in inclusions_list 
            if item['category'].strip() == category
        ]
        
        # Store inclusions
        category_inclusions[category] = category_items
        
        unique_inclusions = defaultdict(set)
        for category, items in category_inclusions.items():
            for item in items:
                unique_inclusions[category].add(item['inclusion'])  


        # Get price for category (taking first non-empty price found)
        price = next((item['price'] for item in category_items if item['price']), "0")
        category_prices[category] = price

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            # registration.user = request.user 
            return redirect('success')
        else:
            print(form.errors)    

    context = {
        'event': event,
        'first_word': first_word,
        'form': form,
        'rest_of_text': rest_of_text,
        'categories': category_list,
        'category_inclusions': category_inclusions,
        'category_prices': category_prices,
        'categories_unique': list(unique_inclusions.keys()),

    }
    
    return render(request, 'event_registration.html', context)



