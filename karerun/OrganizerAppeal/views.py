from django.shortcuts import render,redirect
from RegLogCreate.models import User
from .models import OrganizerAppeal
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
        print(f"userID: {userID} Has Reqeusted to be an Organizer")
        appeal = OrganizerAppeal(user = user)
        appeal.save()
    else:
        print("no session")

    return redirect('homepage')
    
def appealList(request):
   
    userID = request.session.get('userID',None)
    context = {
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

    return render(request,'appealList.html',context)   