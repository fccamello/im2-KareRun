from django.db import models
from RegLogCreate.models import Event
from RegLogCreate.models import User

AGE_CHOICES = [
    ('20 and below', '20 and below'),
    ('21 to 30', '21 to 30'),
    ('31 to 40', '31 to 40'),
    ('41 to 50', '41 to 50'),
    ('51 and above', '51 and above'),
]

class Registration(models.Model):
    registrationid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='registrations', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='registrations', on_delete=models.CASCADE)

    gender = models.CharField(max_length=100, default='M') 
    contactnum = models.CharField(max_length=15, default='000')
    emergencynum = models.CharField(max_length=15, default='000')

    age_category = models.CharField(max_length=30, choices=AGE_CHOICES, default='20 and below')  
    category_ni = models.CharField(max_length=100, default="3k") 
    inclusions = models.CharField(max_length=100, default='0')
    category_price = models.DecimalField(max_digits=10, decimal_places=2)

    registration_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.user.username} - {self.event.eventname} - {self.category_ni}"

    def inclusion_sizes(self):
        return [f"{key}: {value} km" for key, value in self.inclusions.items()]
