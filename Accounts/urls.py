from django.urls import path
from . import views

urlpatterns = [
    path('login', views.UserLogin, name='UserLogin'),
    path('logout', views.UserLogout, name='UserLogout'),
]