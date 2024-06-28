from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm
from listings.models import Listing
from users.models import CustomUser

@login_required
def send_message(request, listing_id, receiver_id):
    listing = get_object_or_404(Listing, id=listing_id)
    receiver = get_object_or_404(CustomUser, id=receiver_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.listing = listing
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('listing_detail', slug=listing.slug)
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form, 'listing': listing, 'receiver': receiver})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent_messages.html', {'messages': messages})
