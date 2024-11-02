from django.shortcuts import render


def index(request):
    userId = request.session.get('userID',None)
    if userId is not None:
        print(userId)
    else:
        print("no session")
    return render(request, 'index.html')

# Create your views here.
