from django.db import models
from RegLogCreate.models import User
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='event_covers/', null=True, blank=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    payment_status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Cancelled', 'Cancelled')])
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.name}"
