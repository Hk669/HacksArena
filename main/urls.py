from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<str:pk>/', views.event_page, name='event_page'),
    path('event-conf/<str:pk>/', views.event_conf, name='event_conf'),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.custom_login, name="login"),
    path('register/', views.register_page, name="register"),
    path('profile/<str:pk>', views.user_page, name="profile"),
    path('project-submission/<str:pk>/', views.project_submission, name="project_submission"),
    path('update-submission/<str:pk>/', views.update_submission, name="update_submission"),
    path('events/', views.search_events, name="search_events"),
    path('hackers/',views.search_profile, name="search_profile"),
    path('accounts/login', views.custom_login, name="custom-login"),
    # path('accounts/github/login/', views.github_login, name="github_login"),
    # path('accounts/github/login/callback/', views.github_callback, name='github_callback'),
]
