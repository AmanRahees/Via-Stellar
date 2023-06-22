from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Accounts.models import *

# Create your views here.

def Via_page(request):
    return render(request, 'ViaStellar.html')

def home(request):
    return render(request, 'home.html')

def settings(request):
    user = User_Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        profile_name = request.POST.get('profile_name')
        about = request.POST.get('about')
        if profile_name != None and about != None:
            user.profile_name = profile_name
            user.about = about
            user.save()
        elif profile_name != None and about == None:
            user.profile_name = profile_name
            user.save()
        elif profile_name == None and about != None:
            user.about = about
            user.save()
    return render(request, 'settings.html')

def change_picture(request):
    try:
        user = Profile_pic.objects.get(user=request.user.id)
    except:
        user = Profile_pic(user=request.user)
    if request.method == 'POST':
        picture = request.FILES.get('picture')
        if picture:
            user.picture = picture
            print(picture)
            user.save()
        return redirect('settings')

def AddFriends(request):
    users = User_Profile.objects.filter(status=False).exclude(user=request.user)
    dp = Profile_pic.objects.all().order_by('user').exclude(user=request.user)
    users_details = zip(users, dp)
    context = {
        'users': users_details,
    }
    return render(request, 'AddFriend.html', context)

def chats(request):
    return render(request, 'chat.html')