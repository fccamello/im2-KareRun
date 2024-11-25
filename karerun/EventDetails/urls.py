from django.urls import path
from .views import event_detail, update_event_photo
urlpatterns = [
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/updateimage/<int:event_id>/', update_event_photo, name='update_event_photo'),
]
