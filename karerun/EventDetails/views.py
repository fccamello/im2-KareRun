import datetime
from django.shortcuts import render, get_object_or_404, redirect
from RegLogCreate.models import Event, User 
from collections import defaultdict
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import json, os, logging
from django.http import JsonResponse
from RegLogCreate.forms import CreateEvent
from EventRegistration.models import Registration

def event_detail(request, event_id):

    #simple set-up for context    
    event = get_object_or_404(Event, eventid=event_id) 
    userId = request.session.get('userID',None)
    user = User.objects.get(userid=userId)
    user_ids = Registration.objects.filter(event=event_id).values_list('user', flat=True)
    participants = User.objects.filter(userid__in=user_ids)
    eventname_split = event.eventname.split(' ', 1)
    first_word = eventname_split[0]
    rest_of_text = " ".join(eventname_split[1:]) if len(eventname_split) > 1 else ''

    inclusions_list = json.loads(event.inclusions) if isinstance(event.inclusions, str) else event.inclusions

    category_inclusions = {}
    category_prices = {}

    
    event_datetime = datetime.datetime.combine(event.eventdate, datetime.time.min)

    # for the date timer
    current_time = datetime.datetime.now()
    time_left = event_datetime - current_time


    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60
    seconds_left = time_left.seconds % 60

    #For Context Stuff
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
    
    #checks for Post Reuqests/Updates
    if request.method == 'POST':
        print("received event POST")
        form = CreateEvent(request.POST, request.FILES, instance=event)  # Bind the form to the existing event
        if form.is_valid():
            # Save the form, which will update the existing event object
            form.save()
            print("updated event")
            return redirect('event_detail', event_id=event.eventid)  # Redirect to the updated event page
        else:
            print(form.errors)
    else:
        form = CreateEvent(instance=event)  # Prefill the form with the current event data
    #Get number of participants
    num_registrants = Registration.objects.filter(event = event).count()

    #Check if user is the organizer/is_superUser
    is_Edit_Allowed = False
    if user.is_superuser or user.userid == event.organizerId:
        is_Edit_Allowed = True


    print("Banner Image URL:", event.bannerimage.url) 
    return render(request, 'event_details.html', {
        'userName': "this is not needed",
        'event': event,
        'userID': userId,
        'forms': form,
        'participants': participants,
        'first_word': first_word,
        'rest_of_text': rest_of_text,
        'categories': category_list,
        'unique_inclusions': unique_inclusions_dict,
         'category_prices': category_prices,
        'num_registrants': num_registrants,
         'days_left': days_left,
        'hours_left': hours_left,
        'minutes_left': minutes_left,
        'is_Super':is_Edit_Allowed,
        'seconds_left': seconds_left,
    })

def update_event_photo(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, eventid=event_id)  # Get the Event object
        photo_type = request.POST.get('type')  # Type of photo being updated
        photo_file = request.FILES.get('photo')  # Uploaded file

        if not photo_file:
            return JsonResponse({'success': False, 'message': 'No file uploaded.'}, status=400)

        # Determine which field to update
        if photo_type == 'banner':
            if event.bannerimage:
                _delete_file(event.bannerimage.path)  # Delete old file
            event.bannerimage = photo_file
        elif photo_type == 'inclusion':
            if event.inclusionimage:
                _delete_file(event.inclusionimage.path)  # Delete old file
            event.inclusionimage = photo_file
        elif photo_type == 'raceroute':
            if event.racerouteimage:
                _delete_file(event.racerouteimage.path)  # Delete old file
            event.racerouteimage = photo_file
        else:
            return JsonResponse({'success': False, 'message': 'Invalid photo type.'}, status=400)

        # Save the event
        event.save()

        # Return the new URL
        return JsonResponse({
            'success': True,
            'new_url': event.bannerimage.url if photo_type == 'banner' else (
                event.inclusionimage.url if photo_type == 'inclusion' else event.racerouteimage.url
            )
        })

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

def _delete_file(file_path):
    """Helper function to delete a file."""
    if os.path.isfile(file_path):
        os.remove(file_path)