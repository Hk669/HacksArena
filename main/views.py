from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Event, Userpoints
from django.contrib.auth import logout
from django.http import HttpResponseNotFound
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
from datetime import datetime
from django.contrib import messages

# redis cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.cache import get_cache_key

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# def cache_key_func(request, *args, **kwargs):
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         return f"{request.path}:{query}"

# def get_or_set_cache(request, cache_key, timeout, callback):
#     data = cache.get(cache_key)
#     if data is None:
#         data = callback()
#         cache.set(cache_key, data, timeout)
#     return data

# @cache_page(60 * 15)  # Cache for 15 minutes 
# def search_events(request):
#     cache_key = cache_key_func(request)
#     return get_or_set_cache(request, cache_key, 60 * 15, lambda: _search_events(request))

# @cache_page(60 * 15)  
# def search_profile(request):
#     cache_key = cache_key_func(request)
#     return get_or_set_cache(request, cache_key, 60 * 15, lambda: _search_profile(request))



# no login views
def home(request):
    users = User.objects.filter(hackathon_participant=True)
    events = Event.objects.all()
    context = {'users':users,'events':events}
    return render(request, 'home.html', context)


def user_page(request, slug):
    user = get_object_or_404(User,slug=slug)
    user_points, created = Userpoints.objects.get_or_create(user=user)

    context = {'user': user, 'user_points':user_points}
    return render(request, 'profile.html', context)


def profile(request, slug):
    if request.user.username.lower() != slug:
        return redirect('home')
    
    user = User.objects.filter(username=slug).first()
    if not user:
        return redirect('home')
    
    user_points, created = Userpoints.objects.get_or_create(user=user)

    form = UserUpdateForm(instance=user)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
                          
    context = {'user':user, 'form':form, 'user_points':user_points}
    return render(request, 'account.html',context)

# @cache_page(CACHE_TTL)
def search_events(request):
    events = Event.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {'events': events, 'form': form}
    return render(request, 'allevents.html', context)

# @cache_page(CACHE_TTL)
def search_profile(request):
    users = User.objects.filter(hackathon_participant=True)
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        users = users.filter(Q(username__icontains=query) | Q(name__icontains=query))
    context = {'users': users, 'form':form}
    return render(request, 'hackers.html',context)



# event views
# @cache_page(CACHE_TTL)
def event_page(request, slug):
    event = get_object_or_404(Event,slug=slug)
    now = datetime.now()
    context = {'event':event, 'now':now }
    return render(request, 'event.html', context)

@login_required()
def event_conf(request, slug):
    event = get_object_or_404(Event,slug=slug)

    if request.method == 'POST':
        event.participants.add(request.user)

        user_points , created = Userpoints.objects.get_or_create(user=request.user)
        user_points.points += 40
        user_points.save()
        messages.success(request, '40 points earned 🌟')


        return redirect('event_page', slug=slug)
    
    return render(request, 'event_conf.html', {'event':event})

@login_required()
def project_submission(request, slug):
    event = get_object_or_404(Event,slug=slug)

    form = SubmissionForm()

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant = request.user
            submission.event = event
            submission.save()

            user_points, created = Userpoints.objects.get_or_create(user=request.user)
            user_points.points += 100
            user_points.save()
            messages.success(request, '100 points earned 🌟')

            
            return redirect('event_page', slug=event.slug)

    context = {'event': event, 'form': form}
    return render(request, 'submission.html', context)

@login_required()
def update_submission(request, slug):
    submission = get_object_or_404(Submission,slug=slug)

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

#blog posts

# @cache_page(CACHE_TTL)
def blog_home(request):
    posts = Posts.objects.all()
    return render(request, "blogs/bloghome.html", {'posts': posts})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            user_points, created = Userpoints.objects.get_or_create(user=request.user)
            user_points.points += 35
            user_points.save()
            messages.success(request, '35 points earned 🌟')

            return redirect('blog-home')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/blogpost.html', {'form': form})


@login_required
def delete_blog(request, slug):
    blog_post = get_object_or_404(Posts, slug=slug)

    if request.user == blog_post.author:
        if request.method == 'POST':
            blog_post.delete()
            return redirect('blog-home')
    
        return render(request, 'blogs/deleteblog.html', {'post': blog_post})
    else:
        return render(request, 'blogs/blogdetail.html', {'post': blog_post})

# @cache_page(CACHE_TTL)
def blog_post_detail(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    return render(request, 'blogs/blogdetail.html', {'post':post})

@login_required
def edit_blog(request, slug):
    blog_post = get_object_or_404(Posts, slug=slug)

    if request.user != blog_post.author:
        messages.error(request, "You don't have permission to edit this blog post.")
        return redirect('blog_post_detail', slug=blog_post.slug)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Blog Post "{blog_post.title}" edited successfully')
            return redirect('blog_post_detail', slug=blog_post.slug)
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        form = BlogPostForm(instance=blog_post)

    return render(request, 'blogs/edit_blog.html', {'form': form, 'post': blog_post})

# @cache_page(CACHE_TTL)
def search_blogs(request):
    blogs = Posts.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        blogs = blogs.filter(Q(title__icontains=query))

    return render(request, 'blogs/bloghome.html', {'blogs':blogs, 'form':form})


# error handilng
def handling_404(request, exception):
    return render(request, '404.html', status=404)

def handling_500(request):
    return render(request, '500.html', status=500)