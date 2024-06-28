from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('send_message/<int:listing_id>/<int:receiver_id>/', views.send_message, name='send_message'),
    path('sent_messages/', views.sent_messages, name='sent_messages'),
]
