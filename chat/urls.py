from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_chat, name='user_chat'),
    path('admin-chat/<int:user_id>/', views.admin_chat, name='admin_chat'),
    path('admin-chat-list/', views.admin_chat_list, name='admin_chat_list'),
]
