from django.shortcuts import render
from RegLogCreate.models import User

def index(request):
    userId = request.session.get('userID',None)
    userName = None
    if userId is not None:
        userName = User.objects.get(userid = userId).username
        print(userId)
    else:
        print("no session")
    
    context ={
        'userName':userName
    }

    return render(request, 'index.html', context)

# Create your views here.