from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('listings/create/', views.listing_create, name='listing_create'),
    path('listings/<slug:slug>/', views.listing_detail, name='listing_detail'),
    path('listings/categories/<int:category_id>/', views.category_listings, name='category_listings'),
    path('listings/<slug:slug>/edit/', views.listing_edit, name='listing_edit'),
     ]
