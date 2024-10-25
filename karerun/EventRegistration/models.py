from django.db import models
from RegLogCreate.models import Event
from RegLogCreate.models import User

class Registration(models.Model):
    registrationid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='registrations', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='registrations', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)  
    inclusions = models.JSONField() 

    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Registration of {self.user.username} for {self.event.eventname} in category {self.category}"

    def inclusion_sizes(self):
        return [f"{key}: {value} km" for key, value in self.inclusions.items()]
