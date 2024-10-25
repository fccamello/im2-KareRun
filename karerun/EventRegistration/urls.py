from django.urls import path
from .views import event_reg
urlpatterns = [
    path('eventreg/<int:event_id>/', event_reg, name='event_reg'), 
]
