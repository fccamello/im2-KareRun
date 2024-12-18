from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from RegLogCreate.models import Event,User
from OrganizerAppeal.models import OrganizerAppeal
from EventRegistration.models import Registration
# dont do log-in required
#@login_required
def homepage(request):
    #warning the session might not have 'userID', in normal means they have
    userId = request.session.get('userID',None)

   
    
    event_ids = Registration.objects.filter(user_id=userId).values_list('event', flat=True)
    created_events = Event.objects.filter(organizerId=userId)
    events = Event.objects.filter(eventid__in=event_ids)


    registrations = Registration.objects.filter(user_id=userId, event__in=events)

    event_registration_details = {}
    for registration in registrations:
        event_registration_details[registration.event.eventid] = {
            'gender': registration.gender,
            'contactnum': registration.contactnum,
            'emergencynum': registration.emergencynum,
            'email': registration.email,
            'age_category': registration.age_category,
            'category_ni': registration.category_ni,
            'inclusions': registration.inclusions,
            'category_price': registration.category_price,
            'registration_date': registration.registration_date,
        }


    appeal = OrganizerAppeal.objects.filter(user = User.objects.get(userid = userId))
    requested = False
    organizer_event = events.filter(organizerId = userId )
    if appeal.exists():
        requested = True
        print("You have already requested")
    user = None
    if userId is not None:
        user = User.objects.get(userid = userId)
    else:
        print("no session")
    context = {
        'events': events,
        'organizer_event': organizer_event,
        'userName':user.username,
        'requested':requested,
        'user':user,
        'userId':user.userid,
        'created_events': created_events,
        'event_registration_details': event_registration_details,
    }
    print("rendering homepage") 
    return render(request, 'homepage.html', context)   

def logout(request):
    del request.session['userID']
    return redirect('index')
