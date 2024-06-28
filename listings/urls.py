# listings/urls.py
from django.urls import path
from .views import listing_list, listing_detail, listing_create, category_listings
from . import views

urlpatterns = [
    path('', listing_list, name='listing_list'),
    path('create/', listing_create, name='listing_create'),
    path('<slug:slug>/', listing_detail, name='listing_detail'),
    path('category/<int:category_id>/', category_listings, name='category_listings'),
]
