from django.urls import path
from .views import event_detail
urlpatterns = [
    path('event/<int:event_id>/', event_detail, name='event_detail'), 
]
