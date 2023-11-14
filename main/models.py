from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    hackathon_participant = models.BooleanField(default=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def event_participated(self):
        return self.user.event_set.all()

class Event(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False, blank=False)
    participants = models.ManyToManyField(User, blank=True, related_name='events')
    date = models.DateField()
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