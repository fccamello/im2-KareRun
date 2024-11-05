from django.db import models
from RegLogCreate.models import User
from datetime import date

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    attendees = models.ManyToManyField(User, related_name='joined_events', blank=True)

    def __str__(self):
        return self.event_name

class UserProfile(models.Model):
    cover_photo = models.ImageField(upload_to='cover_images/', default='cover_images/default.jpg')
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, default="None")
    organization = models.CharField(max_length=100, blank=True, default="None")
    friends = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user.username
    
    @property
    def age(self):
        if self.birthdate:
            today = date.today()
            return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return None
