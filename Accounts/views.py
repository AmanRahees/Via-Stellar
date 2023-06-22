from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import *

# Create your views here.

def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(username, password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password incorrect')
                return redirect('UserLogin')
        else:
            return render(request, 'auth/login.html')
        
def UserSignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST['password']
            re_password = request.POST['re_password']
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken.')
                    return redirect('SignUp')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already registered. Please Login.')
                    return redirect('SignUp')
                else:
                    hashed_password = make_password(password)
                    user = User.objects.create(username=username, email=email, password=hashed_password)
                    user.is_active = True
                    user.save()
                    profile = User_Profile.objects.create(user=user, profile_name=username)
                    profile.save()
                    login(request, user)
                    return redirect('settings')
            else:
                messages.info(request, 'Invalid Entry')
                return redirect('SignUp')
        else:
            return render(request, 'auth/SignUp.html')
        
def UserLogout(request):
    logout(request)
    return redirect('UserLogin')

def friend_request(request, id):
    curr_user = request.user
    friend = User_Profile.objects.get(id=id)
    print(curr_user, '--->', friend.user)
    if Friends.objects.filter(user=curr_user, friend=friend.user).exists():
        messages.warning(request, 'Friend Request Already Sent.')
        return redirect('AddFriends')
    req_message = f'{curr_user.username} send a Friend Request'
    add_friend = Friends.objects.create(user=curr_user, friend=friend.user, frnd_requests=req_message)
    add_friend.save()
    messages.success(request, "Friend request sent successfully.")
    return redirect('AddFriends')

def Request_Decision(request, id):
    
    return