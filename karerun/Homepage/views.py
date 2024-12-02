from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from RegLogCreate.models import Event,User
from OrganizerAppeal.models import OrganizerAppeal
from EventRegistration.models import Registration
@login_required
def homepage(request):
    #warning the session might not have 'userID', in normal means they have
    userId = request.session.get('userID',None)
    event_ids = Registration.objects.filter(user_id=userId).values_list('event', flat=True)
    events = Event.objects.filter(eventid__in=event_ids)
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
    }
    return render(request, 'homepage.html', context)   

def logout(request):
    del request.session['userID']
    return redirect('index')
