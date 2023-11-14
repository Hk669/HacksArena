from django.shortcuts import render, redirect
from .models import User, Event, UserProfile
from django.contrib.auth import logout
from django.http import HttpResponseNotFound

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



# login pages
def logout_view(request):
    logout(request)
    return redirect('/')

def custom_login(request):
    return render(request, 'login.html')

def github_login(request):
    return render(request, 'github_login.html')
