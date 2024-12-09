from collections import defaultdict
from django.shortcuts import get_object_or_404, redirect, render

from .models import Registration
from .forms import RegistrationForm
from RegLogCreate.models import Event, User
from datetime import date

import json

def calculate_age(birthdate):
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def determine_age_category(age):
    if age <= 20:
        return "20 and below"
    elif 21 <= age <= 30:
        return "21 to 30"
    elif 31 <= age <= 40:
        return "31 to 40"
    elif 41 <= age <= 50:
        return "41 to 50"
    else:
        return "51 and above"

def event_reg(request, event_id):

    errors = []
    userId = request.session.get('userID', None)
    print(userId)
    user = User.objects.get(userid = userId)
    print(user)
    user_age = calculate_age(user.birthdate)
    age_category = determine_age_category(user_age)

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
        
        #Check If User is already registered
        if Registration.objects.filter(user=user, event=event).exists():
            print("User is already registered")
            errors.append("You are already registered to this event.")
        elif Registration.objects.filter(event=event).count()>= event.maxSlots:
            print("Event is already full")
            errors.append("Event is already full.")
        elif form.is_valid():
            email = form.cleaned_data['email']
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

            request.session['registration_data'] = {
        'gender': gender,
        'email': email,
        'contactnum': contactnum,
        'emergencynum': emergencynum,
        'age_category': age_category,
        'category_ni': category_ni,
        'category_price': category_price,
        'inclusions': inclusions,
        'singlet_size': singlet_size,
        'finisher_size': finisher_size,
    }


            context = {
                'gender': gender,
                'contactnum': contactnum,
                'emergencynum': emergencynum,
                'age_category': age_category,
                'category_ni': category_ni,
                'category_price': category_price,
                'inclusions': inclusions,
                'categories': category_list,
                 'categories_unique': list(unique_inclusions.keys()),
                 'unique_inclusions': unique_inclusions, 
                'event': event,
                'first_word': first_word,
                'rest_of_text': rest_of_text,
                'user' : user,
                'singlet_size': singlet_size, 
                'finisher_size': finisher_size,
                'userName': user.username

            }

            return render(request, 'regsummary.html', context)  
         
        else:
            print(form.errors)      
            print("Form Data:", request.POST)

    print(errors)
    context = {
        'errors':errors,
        'event': event,
        'first_word': first_word,
        'age_category': age_category,
        'rest_of_text': rest_of_text,
        'categories': category_list,
        'category_inclusions': category_inclusions,
        'category_prices': category_prices,
        'categories_unique': list(unique_inclusions.keys()),
        'unique_inclusions': unique_inclusions, 
        'user' : user,
        'userName': user.username
    }
    
    return render(request, 'event_registration.html', context)

def confirm_registration(request, userId, event_id):
    userId = request.session.get('userID', None)

    event = get_object_or_404(Event, eventid=event_id)
    
    

    registration_data = request.session.get('registration_data', {})

    if registration_data:
        user = User.objects.get(userid=userId)
        gender = registration_data.get('gender')
        contactnum = registration_data.get('contactnum')
        emergencynum = registration_data.get('emergencynum')
        age_category = registration_data.get('age_category')
        category_ni = registration_data.get('category_ni')
        inclusions = registration_data.get('inclusions')  # Ensure this is in a format suitable for your database
        category_price = registration_data.get('category_price')


    print("POST Data:", request.POST)
    print("Gender:", gender)
    print("Contact Number:", contactnum)
    print("Emergency Number:", emergencynum)
    print("Age Category:", age_category)
    print("Category:", category_ni)
    print("Inclusions:", inclusions)
    print("Category Price:", category_price)

    registration = Registration(
        user=user,
        event=event,
        gender=gender,
        contactnum=contactnum,
        emergencynum=emergencynum,
        age_category=age_category,
        category_ni=category_ni,
        inclusions=inclusions,
        category_price=category_price
    )
    registration.save()
    return redirect('index')  