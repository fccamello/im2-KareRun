from django.shortcuts import render, redirect, get_object_or_404
from RegLogCreate.models import User
from .forms import UserProfileForm
from .models import UserProfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.core.files.storage import default_storage
from EventRegistration.models import Registration
from RegLogCreate.models import Event

def view_profile(request, username):
    # Get the user by username
    user = get_object_or_404(User, username=username)
    
    # Fetch the user profile (assuming the user profile is related to the User model via OneToOneField)
    profile = get_object_or_404(UserProfile, user=user)
    event_ids = Registration.objects.filter(user_id=user.userid).values_list('event', flat=True)
    registered_events = Event.objects.filter(eventid__in=event_ids)
    created_events = Event.objects.filter(organizerId=user.userid)
    return render(request, 'view_profile.html', {'user': user, 'profile': profile, 'userName': user.username, 'registered_events': registered_events, 'created_events': created_events,})

@login_required
@csrf_exempt
def update_profile(request, username):
    if request.method == 'POST':
        data = json.loads(request.body)
        field = data.get('field')
        value = data.get('value')

        try:
            user = User.objects.get(username=username)
            profile = UserProfile.objects.get(user=user)

            if field == 'bio':
                profile.bio = value
            elif field == 'birthdate':
                profile.birthdate = value
            elif field == 'age':
                profile.age = value
            elif field == 'gender':
                profile.gender = value
            elif field == 'organization':
                profile.organization = value

            profile.save()
            return JsonResponse({'success': True})

        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User not found'}, status=404)

    return JsonResponse({'success': False}, status=400)

@csrf_exempt
def update_photo(request, username):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        photo_type = request.POST.get('type')  
        if photo:
            # Logic to save the new photo
            user = User.objects.get(username=username)
            profile = UserProfile.objects.get(user=user)
            if photo_type == 'cover':
                profile.cover_photo = photo
            else:
                profile.profile_image = photo
            profile.save()
            return JsonResponse({'success': True, 'new_url': profile.cover_photo.url if photo_type == 'cover' else profile.profile_image.url})
    return JsonResponse({'success': False})