from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/update/', views.update_event_detail, name='update_event_detail'),
    path('event/<int:event_id>/cover_photo/', views.update_event_cover_photo, name='update_event_cover_photo'),
]
