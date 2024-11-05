from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Event, Participant
from .forms import EventForm
import json

@login_required
def organizer_event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participants = event.participants.all()
    return render(request, 'event_detail.html', {
        'event': event,
        'participants': participants,
    })

@require_POST
@login_required
def update_event_detail(request, event_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        field = data.get('field')
        value = data.get('value')

        try:
            event = Event.objects.get(id=event_id)

            if field == 'name':
                event.name = value
            elif field == 'description':
                event.description = value
            elif field == 'date':
                event.date = value
            elif field == 'location':
                event.location = value

            event.save()
            return JsonResponse({'success': True})

        except Event.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Event not found'}, status=404)

    return JsonResponse({'success': False}, status=400)

@require_POST
@login_required
def update_event_cover_photo(request, event_id):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        photo_type = request.POST.get('type')  
        if photo:
            # Logic to save the new photo
            event = Event.objects.get(id=event_id)
            event.cover_photo = photo
            event.save()
            return JsonResponse({'success': True, 'new_url': event.cover_photo.url})
    return JsonResponse({'success': False})
