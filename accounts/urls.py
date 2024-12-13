from django.urls import path
from . import views


urlpatterns = [
    # path('register/', views.register, name='signup'),
    path('register/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]