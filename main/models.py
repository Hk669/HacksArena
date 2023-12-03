from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    hackathon_participant = models.BooleanField(default=True, null=True)
    avatar = models.ImageField(default='default.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    #socials
    twitter = models.URLField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=500, null=True, blank=True)
    github = models.URLField(max_length=500, null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def event_participated(self):
        return self.user.event_set.all()

class Event(models.Model):
    avatar = models.ImageField(default='default1.png')
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False, blank=False)
    participants = models.ManyToManyField(User, blank=True, related_name='events')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    reg_deadline = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #SET_NULL will set the submission to null but will store the details of the submission 
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return str(self.event) + ' by ' + str(self.participant)
    

class Posts(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False)
    # image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title