from .views import confirm_registration
from django.urls import path
from .views import event_reg
urlpatterns = [
    path('eventreg/<int:event_id>/', event_reg, name='event_reg'), 
    path('confirm_registration/<int:userId>/<int:event_id>', confirm_registration, name='confirm_registration'),  

]
