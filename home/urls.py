from django.urls import path
from . import views

urlpatterns = [
    path("", views.Via_page, name='via'),
    path("home", views.home, name='home'),
    path("settings", views.settings, name='settings'),
    path("chats", views.chats, name='chats'),
]