from django.urls import path
from . import views

from django.urls import path
from . import views


# chat/urls.py
from django.urls import path
from .views import chat_view, admin_chat_list_view, user_chat_list_view

urlpatterns = [
    path('<int:admin_id>/', chat_view, name='chat_view'),  # چت با ادمین خاص
    path('admin/', admin_chat_list_view, name='admin_chat_list_view'),  # لیست چت ادمین
    path('user/', user_chat_list_view, name='user_chat_list_view'),  # لیست چت کاربران
]