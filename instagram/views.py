from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import Photos, Profile
from .forms import ProfileForm, PhotoForm

def home_page(request):
    '''
    functions for the instagram landing page
    '''
    title = "Instagram | Home"
    images=Photos.display_images()
    return render(request, 'user/index.html', {"title": title, "images":images})


@login_required
def user_profile_edit(request):
    '''
    function for editing user profile
    '''
    current_user=request.user
    form=ProfileForm()
    if Profile.objects.filter(user_id=current_user.id).exists():
        Profile.objects.filter(user_id=current_user.id).delete()
        print("You can only have one profile")
        if request.method=='POST':
            current_user=request.user
            print(current_user)
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.user=current_user
                profile.save()

    else:
        if request.method=='POST':
            current_user=request.user
            print(current_user)
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.user=current_user
                profile.save()
        else:
            form=ProfileForm()
    title="Instagram | Profile Edit "
    return render(request, 'user/profile_edit.html', {"title":title, "form":form})

def user_upload_images(request):
    '''
    function for the form uploading images to 
    instagram
    '''
    current_user=request.user
    if request.method=='POST':
        form=PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.profile=current_user
            photo.save()

    else:
        form =PhotoForm()

    return render(request, 'user/photo.html', {"form":form})

def user_profile(request):
    current_user=request.user
    title=f'Instagram | {current_user.username}'
    profile = Profile.objects.get(user_id=current_user.id)
    images = Photos.objects.all().filter(profile_id=current_user.id)

    
    
    return render(request, 'user/profile.html', {"title":title,"profiles":profile, "images":images})
