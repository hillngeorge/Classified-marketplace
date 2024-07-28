from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordResetForm, CustomSetPasswordForm, CustomAuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from listings.models import Listing, Category
from listings.forms import ListingForm  # Corrected import statement
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data["username"].capitalize()
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
def login_view(request):    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print("Invalid form")
            print(form.errors.as_json())
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = '/'

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/profile.html', {'u_form': form})

def home(request):
    categories = Category.objects.all().order_by('name')  # Order categories alphabetically
    listings = Listing.objects.all()[:10]  # Assuming you want the first 10 listings
    context = {
        'categories': categories,
        'listings': listings,
    }
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'users/contact.html')

def activity_feed(request):
    recent_listings = Listing.objects.order_by('-created_at')[:10]
    return render(request, 'users/activity_feed.html', {'recent_listings': recent_listings})

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'users/password_reset.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'users/password_reset_confirm.html'
