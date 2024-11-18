from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
import datetime
# Create your models here.
#add db_comment && 
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)


   
class User(AbstractBaseUser, PermissionsMixin):
    userid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    isEventOrganizer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    userType = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(3)])
    sex = models.CharField(max_length=10)
   
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']  # Fields required for superuser creation

    def __str__(self):
        return self.username

#should be hashed by django
    def login(email,password):
        # hashedPassword = make_password(password)
        hashedPassword = password
        print(email)
        print(password)
        user = authenticate(email=email, password=hashedPassword)
        if user is not None:
            return user
        else:
            return None
        


# bannerloc = FileSystemStorage(location="./photos/eventbanner/")
# inclusionloc = FileSystemStorage(location="./photos/eventinclusion/")
# sizechartloc = FileSystemStorage(location="./photos/eventsizechart/")
# racerouteloc = FileSystemStorage(location="./photos/eventraceroute/")

class Event(models.Model):
    eventid = models.BigAutoField(primary_key=True)
    organizerId = models.IntegerField(default=0)
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