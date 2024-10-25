from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
import datetime
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
    birthdate = models.DateField(null = True, blank = True)
    isEventOrganizer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

#should be hashed by django
    def login(email,password):
        # hashedPassword = make_password(password)
        hashedPassword = password
        User.objects.filter(email = email).filter(password = hashedPassword).get()


# bannerloc = FileSystemStorage(location="./photos/eventbanner/")
# inclusionloc = FileSystemStorage(location="./photos/eventinclusion/")
# sizechartloc = FileSystemStorage(location="./photos/eventsizechart/")
# racerouteloc = FileSystemStorage(location="./photos/eventraceroute/")

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
    # bannerimage = models.ImageField(storage=bannerloc)
    # inclusionimage = models.ImageField(storage=inclusionloc)
    # sizechartimage = models.ImageField(storage=sizechartloc)
    # racerouteimage = models.ImageField(storage=racerouteloc)


    bannerimage = models.ImageField(upload_to='eventbanner/')
    inclusionimage = models.ImageField(upload_to='eventinclusion/')
    sizechartimage = models.ImageField(upload_to='eventsizechart/')
    racerouteimage = models.ImageField(upload_to='eventraceroute/')

    def __str__(self) -> str:
        return self.eventname