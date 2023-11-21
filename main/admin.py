from django.contrib import admin
from .models import User, Event, Submission, Posts
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Posts)
admin.site.register(Submission)

from allauth.socialaccount.models import SocialAccount

class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid', 'extra_data')
    search_fields = ('user__username', 'uid', 'extra_data')