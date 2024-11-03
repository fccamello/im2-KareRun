from django.db import models
from RegLogCreate.models import User
# Create your models here.


class OrganizerAppeal(models.Model):
    appealID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    isAccepted = models.BooleanField(default=False)
    acceptedBy = models.IntegerField(default=-1)
    def __str__(self):
        return self.user.username