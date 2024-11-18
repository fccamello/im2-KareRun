from collections import defaultdict
from django.shortcuts import get_object_or_404, redirect, render

from .models import Registration
from .forms import RegistrationForm
from RegLogCreate.models import Event, User
import json

def event_reg(request, event_id):

    userId = request.session.get('userID', None)
    user = User.objects.get(userid = userId)

    event = get_object_or_404(Event, eventid=event_id)    
    eventname_split = event.eventname.split(' ', 1)
    first_word = eventname_split[0]
    rest_of_text = eventname_split[1] if len(eventname_split) > 1 else ''
    
    categories = event.eventcategory.split(',')
    category_list = [category.strip() for category in categories]

    print("Categories:", category_list)

    inclusions_list = json.loads(event.inclusions) if isinstance(event.inclusions, str) else event.inclusions
    
    category_inclusions = {}
    category_prices = {}
    
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


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            gender = form.cleaned_data['gender']
            contactnum = form.cleaned_data['contact_number']
            emergencynum = form.cleaned_data['emergency_number']
            age_category = form.cleaned_data['age_category']
            category_ni = form.cleaned_data['category_ni']
            category_price = form.cleaned_data['category_price']
            singlet_size = form.cleaned_data['singlet_size']
            finisher_size = form.cleaned_data['finisher_shirt_size']

            inclusions = {
                'inclusions': [],  
                'singlet_size': request.POST.get('singlet_size'),
                'finisher_shirt_size': request.POST.get('finisher_shirt_size')
            }

            if category_ni in category_inclusions:
                inclusions['inclusions'] = [
                    {key: item[key] for key in item if key != 'price'}
                    for item in category_inclusions[category_ni]
                    if item['inclusion'] not in ['Finisher Shirt', 'Singlet']
                ]

                singlet_size_set =  False
                for item in category_inclusions[category_ni]:
                    if item['inclusion'] == 'Finisher Shirt':
                        inclusions['finisher_shirt_size'] = finisher_size 
                    elif item['inclusion'] == 'Singlet':
                        inclusions['singlet_size'] = singlet_size
                        singlet_size_set = True
                        print(item['size'])
            
            registration = Registration(
            user = User.objects.get(userid=userId), 
            event = event,
            gender = gender,
            contactnum = contactnum,
            emergencynum = emergencynum,
            age_category = age_category,
            category_ni = category_ni,
            inclusions = inclusions,
            category_price=category_price
            )
            registration.save()
            return redirect('index')
        else:
            print(form.errors)      
            print("Form Data:", request.POST)



    context = {
        'event': event,
        'first_word': first_word,
        'rest_of_text': rest_of_text,
        'categories': category_list,
        'category_inclusions': category_inclusions,
        'category_prices': category_prices,
        'categories_unique': list(unique_inclusions.keys()),
        'unique_inclusions': unique_inclusions, 
        'user' : user
    }
    
    return render(request, 'event_registration.html', context)





