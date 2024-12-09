from django.db import models
from RegLogCreate.models import User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    cover_photo = models.ImageField(upload_to='photos/', default='photos/defaultbg.png')
    profile_image = models.ImageField(upload_to='photos/', default='photos/default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    organization = models.CharField(max_length=100, blank=True, default="None")
    friends = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user.username
    
    @property
    def age(self):
        if self.user.birthdate:
            today = date.today()
            return today.year - self.user.birthdate.year - ((today.month, today.day) < (self.user.birthdate.month, self.user.birthdate.day))
        return None

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()