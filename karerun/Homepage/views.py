from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from RegLogCreate.models import Event,User
from OrganizerAppeal.models import OrganizerAppeal
@login_required
def homepage(request):
    events = Event.objects.all()

    #warning the session might not have 'userID', in normal means they have
    userId = request.session.get('userID',None)
    user = User.objects.get(userid=userId)

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
        'events': organizer_event,
        'organizer_event': organizer_event,
        'userName':user.username,
        'requested':requested,
        'user':user
    }
    return render(request, 'homepage.html', context)   

def logout(request):
    del request.session['userID']
    return redirect('index')
