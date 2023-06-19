from django.shortcuts import render
from django.contrib.auth.models import User
from Accounts.models import *

# Create your views here.

def Via_page(request):
    return render(request, 'ViaStellar.html')

def home(request):
    user = User_Profile.objects.get(user=request.user.id)
    user_pfn = user.profile_name
    user_abt = user.about
    context = {
        'user_pfn': user_pfn,
        'user_abt': user_abt,
    }
    return render(request, 'home.html', context)

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
    user_pfn = user.profile_name
    user_abt = user.about
    context = {
        'user_pfn': user_pfn,
        'user_abt': user_abt,
    }
    return render(request, 'settings.html', context)

def chats(request):
    return render(request, 'chat.html')