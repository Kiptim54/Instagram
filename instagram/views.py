from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import Photos

def home_page(request):
    title = "Instagram | Home"
    images=Photos.display_images()
    return render(request, 'user/index.html', {"title": title, "images":images})
@login_required
def user_profile(request):
    title="Instagram | Home "
    return render(request, 'user/profile.html', {"title":title})
