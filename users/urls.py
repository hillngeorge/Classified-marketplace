from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='my_login'),
    path('logout/', views.logout_view, name='my_logout'),
    path('contact', views.contact, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', views.home, name='home'),
    path('activity_feed/', views.activity_feed, name='activity_feed'),
]
