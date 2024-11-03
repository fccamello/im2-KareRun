from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/update/<int:event_id>/', views.update_event_detail, name='update_event_detail'),
    path('event/cover_photo/<int:event_id>/', views.update_event_cover_photo, name='update_event_cover_photo'),
]
