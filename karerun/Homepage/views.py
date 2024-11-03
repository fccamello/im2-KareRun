from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RegLogCreate.models import Event

@login_required
def homepage(request):
    events = Event.objects.all()
    return render(request, 'homepage.html', {'user': request.user, 'events':events})
