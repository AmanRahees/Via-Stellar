from django.urls import path
from . import views

urlpatterns = [
    path("", views.Via_page, name='via'),
    path("home", views.home, name='home'),
    path("settings", views.settings, name='settings'),
    path("pic_update", views.change_picture, name='pic_update'),
    path("AddFriends", views.AddFriends, name='AddFriends'),
    path("chats", views.chats, name='chats'),
]