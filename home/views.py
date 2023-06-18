from django.shortcuts import render

# Create your views here.

def Via_page(request):
    return render(request, 'ViaStellar.html')

def home(request):
    return render(request, 'home.html')

def settings(request):
    return render(request, 'settings.html')