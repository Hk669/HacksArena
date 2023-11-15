from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Event, Submission

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['details']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')