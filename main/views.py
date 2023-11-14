from django.shortcuts import render, redirect
from .models import User, Event, UserProfile
from django.contrib.auth import logout
from django.http import HttpResponseNotFound
from .forms import *


def home(request):
    users = User.objects.filter(hackathon_participant=True)
    events = Event.objects.all()
    context = {'users':users,'events':events}
    return render(request, 'home.html', context)

def user_page(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)



# event views
def event_page(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request, 'event.html', context)

def event_conf(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event_page', pk=event.id)
    
    return render(request, 'event_conf.html', {'event':event})

def project_submission(request, pk):
    event = Event.objects.get(id=pk)

    form = SubmissionForm()

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant = request.user
            submission.event = event
            submission.save()
            
            return redirect('profile', pk=pk)

    context = {'event': event, 'form': form}
    return render(request, 'submission.html', context)


# login pages
def logout_view(request):
    logout(request)
    return redirect('/')

def custom_login(request):
    return render(request, 'login.html')

def github_login(request):
    return render(request, 'github_login.html')
