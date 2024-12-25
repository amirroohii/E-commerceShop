# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import ChatMessage
from accounts.models import User

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import ChatMessage

# View for handling chat with a specific admin
@login_required
def chat_view(request, admin_id):
    # Retrieve the admin user object based on the provided admin_id, or return a 404 error if not found
    admin_user = get_object_or_404(User, id=admin_id)

    # Check if the request method is POST (indicating a message is being sent)
    if request.method == 'POST':
        # Get the message content from the POST data
        content = request.POST.get('message')
        if content:  # Ensure that the message is not empty
            # Create a new chat message from the user to the admin
            ChatMessage.objects.create(user=request.user, admin=admin_user, message=content, is_from_admin=False)
            # Redirect back to the chat view for the same admin
            return redirect('chat_view', admin_id=admin_id)

    # Retrieve chat messages between the user and the admin
    messages = ChatMessage.objects.filter(
        Q(user=request.user, admin=admin_user) | Q(user=admin_user, admin=request.user)
    ).order_by('timestamp')  # Order messages by timestamp

    # Render the chat template with the messages and the admin user information
    return render(request, 'chat/chat.html', {'messages': messages, 'admin_user': admin_user})

# View for displaying a list of chats with regular users for admins
@login_required
def admin_chat_list_view(request):
    # Retrieve all users who are not staff (regular users)
    users = User.objects.filter(is_staff=False)  # Only regular users
    # Render the admin chat list template with the list of users
    return render(request, 'chat/admin_chat_list.html', {'users': users})

# View for displaying a list of chats with admins for regular users
@login_required
def user_chat_list_view(request):
    # Retrieve all users who are staff (admins)
    admins = User.objects.filter(is_staff=True)  # Only admins
    # Render the user chat list template with the list of admins
    return render(request, 'chat/user_chat_list.html', {'admins': admins})