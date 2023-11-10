from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<str:pk>/', views.event_page, name='event_page'),
    path('event-conf/<str:pk>/', views.event_conf, name='event_conf'),
    path('logout/', views.logout_view, name="logout"),
]
