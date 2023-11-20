from django.shortcuts import render, redirect
from .models import User, Event, UserProfile
from django.contrib.auth import logout
from django.http import HttpResponseNotFound
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# no login views
def home(request):
    users = User.objects.filter(hackathon_participant=True)
    events = Event.objects.all()
    context = {'users':users,'events':events}
    return render(request, 'home.html', context)

def user_page(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)

def search_events(request):
    events = Event.objects.all()

    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {'events': events, 'form': form}
    return render(request, 'allevents.html', context)

def search_profile(request):
    users = User.objects.filter(hackathon_participant=True)

    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        users = users.filter(Q(username__icontains=query) | Q(name__icontains=query))
    context = {'users': users, 'form':form}
    return render(request, 'hackers.html',context)



# event views
def event_page(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request, 'event.html', context)

@login_required()
def event_conf(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event_page', pk=event.id)
    
    return render(request, 'event_conf.html', {'event':event})

@login_required()
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

@login_required()
def update_submission(request, pk):
    submission = Submission.objects.get(id=pk)

    if request.user != submission.participant:
        return HttpResponse("You're not allowed :)")
    
    event = submission.event
    form = SubmissionForm(instance=submission)

    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'event':event}
    return render(request, 'submission.html', context)



# login pages
def custom_login(request):
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'],
                            password= request.POST['password'])
        
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def register_page(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            return redirect('home')
    return render(request, 'register.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def github_login(request):
    return render(request, 'github_login.html')
