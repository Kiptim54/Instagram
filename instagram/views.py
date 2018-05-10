from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import Photos, Profile
from .forms import PhotoForm

def home_page(request):
    title = "Instagram | Home"
    images=Photos.display_images()
    return render(request, 'user/index.html', {"title": title, "images":images})
@login_required
def user_profile(request):
    if request.method=='POST':
        current_user=request.user
        print(current_user)
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.user=current_user
            photo.save()
    else:
        form=PhotoForm()
    title="Instagram | Home "
    return render(request, 'user/profile.html', {"title":title, "form":form})
