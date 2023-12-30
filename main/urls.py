from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<slug:slug>/', views.event_page, name='event_page'),
    path('event-conf/<slug:slug>/', views.event_conf, name='event_conf'),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.custom_login, name="login"),
    path('register/', views.register_page, name="register"),
    path('profile/<slug:slug>', views.user_page, name="profile"),
    path('project-submission/<str:pk>/', views.project_submission, name="project_submission"),
    path('update-submission/<str:pk>/', views.update_submission, name="update_submission"),
    path('events/', views.search_events, name="search_events"),
    path('hackers/',views.search_profile, name="search_profile"),
    path('accounts/login', views.custom_login, name="custom-login"),
    path('account/<slug:slug>/', views.profile, name="account"),
    # path('accounts/github/login/', views.github_login, name="github_login"),
    # path('accounts/github/login/callback/', views.github_callback, name='github_callback'),
    path('blogs/',views.search_blogs, name='blog-home'),
    path('blogpost/', views.create_blog, name='create_blog'),
    path('delete/<slug:slug>/',views.delete_blog, name="delete_blog"),
    path('blog/<slug:slug>/',views.blog_post_detail, name="blog_post_detail"),
    path('blog/<slug:slug>/edit', views.edit_blog, name="edit_blog"),
]
