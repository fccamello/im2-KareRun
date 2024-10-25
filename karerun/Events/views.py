from django.shortcuts import render
from RegLogCreate.models import Event

def race_list_view(request):
    events = Event.objects.all()

    query = request.GET.get('search', '')
    if query:
        events = events.filter(eventname__icontains=query)

    sort_by = request.GET.get('sort', 'date') 
    if sort_by == 'name':
        events = events.order_by('eventname')
    else:
        events = events.order_by('eventdate')

    context = {
        'events': events,
        'search_query': query,
        'sort_by': sort_by,
    }
    return render(request, 'event_list.html', context)
