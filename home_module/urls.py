from . import views
from django.urls import path


urlpatterns =[
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
]