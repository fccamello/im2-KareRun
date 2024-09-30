from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.hashers import make_password
<<<<<<< HEAD
import datetime
=======
>>>>>>> 2ab8c514eddc9bd5460e8aec00c4ad87f4a0a07b
# Create your models here.
#add db_comment && 
class User(models.Model):
    userid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30) #Display Name?
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    #Should be hashed
    password = models.CharField(max_length=255)
    email = models.EmailField()
<<<<<<< HEAD
    birthdate = models.DateField(null = True, blank = True)
=======
    birthdate = models.DateTimeField()
>>>>>>> 2ab8c514eddc9bd5460e8aec00c4ad87f4a0a07b
    isEventOrganizer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

#should be hashed by django
    def login(email,password):
        # hashedPassword = make_password(password)
        hashedPassword = password
        User.objects.filter(email = email).filter(password = hashedPassword).get()

    def register(details: dict) -> bool:
        new_user = User(firstname = details['firstname'],
                        lastname=details['lastname'],
                        birthdate=details['birthdate'],
                        username=details['username'],
                        email = details['email'],
                        password = details['password'])
        new_user.save()
        return True





class Event(models.Model):
    eventid = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=100)
    eventdetails = models.TextField()
    #should be list of categories
    eventcategory  = models.JSONField()
    eventlocation = models.CharField(max_length=100)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    dateposted = models.DateTimeField(auto_now_add=True)
    #should be a list of inclusions
    inclusions = models.JSONField()
    bannerimage = models.ImageField()
    inclusionimage = models.ImageField()
    sizechartimage = models.ImageField()
    racerouteimage = models.ImageField()

    def __str__(self) -> str:
        return self.eventname