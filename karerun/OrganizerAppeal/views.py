from django.shortcuts import render,redirect
from RegLogCreate.models import User, Event
from .models import OrganizerAppeal
from django.db.models import Count

# Create your views here.
def appeal(request):
    userID = request.session.get('userID',None)
    appeal  = OrganizerAppeal.objects.filter(user = User.objects.get(userid = userID))
    user = None
    if userID is not None:
        user = User.objects.get(userid = userID)
    if appeal.exists():
        print("You have already requested")
        redirect('homepage')
    elif User.objects.get(userid = userID).isEventOrganizer == False:
        print(f"userID: {userID} Has Requested to be an Organizer")
        appeal = OrganizerAppeal(user = user)
        appeal.save()
    else:
        print("no session")

    return redirect('homepage')
    
def appealList(request):
   
    events = Event.objects.all()
    users = User.objects.all()

    regular_users_count = User.objects.filter(isEventOrganizer=False, is_superuser=False, is_staff=False).count()
    event_count = Event.objects.count()
    organizer_count = User.objects.filter(isEventOrganizer=True).count()

    gender_distribution = User.objects.values('sex').annotate(count=Count('userid'))
    gender_labels = [entry['sex'] for entry in gender_distribution]
    gender_counts = [entry['count'] for entry in gender_distribution]




    userID = request.session.get('userID',None)
    context = {
        'events': events,
        'users': users,
        'gender_labels': gender_labels,
        'gender_counts': gender_counts,
        'regular_users_count' : regular_users_count,
        'organizer_count' : organizer_count,
        'event_count': event_count,
        'appeals':None,
        'userName':None
    }
    if userID is not None:
        context['userName'] = User.objects.get(userid = userID).username
    if userID is not None and User.objects.get(userid = userID).is_staff == True:
        appeals = OrganizerAppeal.objects.filter(acceptedBy = -1)
        context['appeals'] = appeals
    else:#if not admin
        return redirect('homepage')

    if request.method == 'POST':
        appealID = request.POST.get('appeal_id')
        print(f"appealID: {appealID}")
        action = request.POST.get('action')
        if action == "accept":
            appeal = OrganizerAppeal.objects.get(appealID = appealID)
            appeal.isAccepted = True
            appeal.acceptedBy = userID
            appeal.user.isEventOrganizer = True
            appeal.user.save()
            appeal.save()
            print("appeal accepted")
        elif action == "decline":
            appeal = OrganizerAppeal.objects.get(appealID = appealID)
            appeal.delete() 



    return render(request,'appealList.html',context)   