from django.shortcuts import render
from RegLogCreate.models import Event, User

def race_list_view(request):
    events = Event.objects.all()

    query = request.GET.get('search', '')
    if query:
        events = events.filter(eventname__icontains=query)

    categories = request.GET.getlist('category')  
    if categories:
        events = events.filter(eventcategory__in=categories)  

    sort_by = request.GET.get('sort', 'date')
    if sort_by == 'name':
        events = events.order_by('eventname')
    else:
        events = events.order_by('eventdate')

    userId = request.session.get('userID', None)
    userName = None
    if userId is not None:
        userName = User.objects.get(userid=userId).username
        print("user id ni", userId)
        print("user name ni", userName)
    else:
        print("no session")

    context = {
        'events': events,
        'search_query': query,
        'sort_by': sort_by,
        'category': categories,  
        'userName': userName,
    }
    return render(request, 'event_list.html', context)
