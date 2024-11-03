# admin.py
from django.contrib import admin
from .models import Event, Participant

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'organizer')
    search_fields = ('name', 'location')
    list_filter = ('date',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'payment_status', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('payment_status', 'event')
