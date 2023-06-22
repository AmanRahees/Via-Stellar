from django.urls import path
from . import views

urlpatterns = [
    path('login', views.UserLogin, name='UserLogin'),
    path('signup', views.UserSignUp, name='SignUp'),
    path('logout', views.UserLogout, name='UserLogout'),
    path('friendRequest/<int:id>', views.friend_request, name='friendRequest'),
]