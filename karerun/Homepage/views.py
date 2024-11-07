from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RegLogCreate.models import Event,User

@login_required
def homepage(request):
    events = Event.objects.all()
    #warning the session might not have 'userID', in normal means they have
    userId = request.session.get('userID',None)
    user = None
    if userId is not None:
        user = User.objects.get(userid = userId)
        print(userId)
    else:
        print("no session")
    return render(request, 'homepage.html', {'user': user, 'events':events})
