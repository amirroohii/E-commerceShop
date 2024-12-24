from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import ChatMessage
from .forms import ChatMessageForm
from accounts.models import User

@login_required
def user_chat(request):
    admin = User.objects.filter(is_superuser=True).first()
    messages = ChatMessage.objects.filter(user=request.user, admin=admin).order_by('timestamp')

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.admin = admin
            message.save()
            return redirect('user_chat')
    else:
        form = ChatMessageForm()

    return render(request, 'chat/user_chat.html', {'messages': messages, 'form': form})


@staff_member_required
def admin_chat(request, user_id):
    user = User.objects.get(id=user_id)
    messages = ChatMessage.objects.filter(user=user, admin=request.user).order_by('timestamp')

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = user
            message.admin = request.user
            message.is_from_admin = True
            message.save()
            return redirect('admin_chat', user_id=user_id)
    else:
        form = ChatMessageForm()

    return render(request, 'chat/admin_chat.html', {'messages': messages, 'form': form, 'chat_user': user})


@staff_member_required
def admin_chat_list(request):
    users_with_chats = User.objects.filter(user_messages__isnull=False).distinct()
    return render(request, 'chat/admin_chat_list.html', {'users': users_with_chats})
