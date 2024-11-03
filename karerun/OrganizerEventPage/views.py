from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Event, Participant
from .forms import EventCoverPhotoForm

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participants = event.participants.all()
    return render(request, 'event_detail.html', {
        'event': event,
        'participants': participants,
    })

@require_POST
@login_required
def update_event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    field = request.POST.get('field')
    value = request.POST.get('value')

    if field and hasattr(event, field):
        setattr(event, field, value)
        event.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@require_POST
@login_required
def update_event_cover_photo(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = EventCoverPhotoForm(request.POST, request.FILES, instance=event)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'new_url': event.cover_photo.url})
    return JsonResponse({'success': False})
