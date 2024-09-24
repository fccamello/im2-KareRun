from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
#add db_comment && 
class User(models.Model):
    userid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    #Should be hashed
    password = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    isEventOrganizer = models.BooleanField(default=False)





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
    