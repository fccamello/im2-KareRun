from django.shortcuts import render,redirect
from RegLogCreate.models import User
from .models import OrganizerAppeal
# Create your views here.
def appeal(request):
    userID = request.session.get('userID',None)
    if userID is not None and User.objects.get(userid = userID).userType == 0:
        print(f"userID: {userID} Has Reqeusted to be an Organizer")
        user = User.objects.get(userid = userID)
        appeal = OrganizerAppeal(user = user)
        appeal.save()
    else:
        print("no session")

    return redirect('index')
    
def appealList(request):
   
    userID = request.session.get('userID',None)
    context = {
        'appeals':None,
        'userName':None
    }
    if userID is not None:
        context['userName'] = User.objects.get(userid = userID).username
    if userID is not None and User.objects.get(userid = userID).userType == 3:
        appeals = OrganizerAppeal.objects.filter(acceptedBy = -1)
        context['appeals'] = appeals
    else:#if not admin
        return redirect('index')

    if request.method == 'POST':
        appealID = request.POST.get('appeal_id')
        print(f"appealID: {appealID}")
        action = request.POST.get('action')
        if action == "accept":
            appeal = OrganizerAppeal.objects.get(appealID = appealID)
            appeal.isAccepted = True
            appeal.acceptedBy = userID
            appeal.save()
            print("appeal accepted")
            user = User.objects.get(userid = appeal.user.userid)
            user.userType = 1
            user.save()

    return render(request,'appealList.html',context)   