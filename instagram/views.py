from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    title = "Instagram | Home"
    return render(request, 'user/index.html', {"title": title})

def user_profile(request):
    title="Instagram | Home "
    return render(request, 'user/index.html', {"title":title})
