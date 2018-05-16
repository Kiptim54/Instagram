from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import Photos, Profile, Comments, Likes
from .forms import ProfileForm, PhotoForm, CommentForm
from django.core.exceptions import ValidationError

@login_required
def home_page(request):
    '''
    functions for the instagram landing page
    '''
    current_user=request.user.id
    title = "Instagram | Home"
    images = Photos.objects.all().filter(profile__user=current_user)
    comments=Comments.objects.all()
    
    return render(request, 'user/index.html', {"title": title, "images":images, "comments":comments})

@login_required
def like_post(request, id):
    current_user=request.user
    photo=get_object_or_404(Photos, id=id)
    if current_user in photo.likes.all():
        photo.likes.add(current_user)
        photo.likes.remove(current_user)
        print(current_user)
        print("hello")
    else:
        photo.likes.add(current_user)
        return redirect('/')
    return redirect('/')
    
    

def explore_page(request):
    '''
    functions for the instagra explore page to see people you do not know
    '''
    current_user=request.user.id
    title = "Instagram | Explore"
    images = Photos.objects.all().exclude(profile__user=current_user)
    comments=Comments.objects.all()
    
    return render(request, 'user/explore.html', {"title": title, "images":images, "comments":comments})

@login_required
def view_image(request, id):
    title="images_details"
    photo=get_object_or_404(Photos, id=id)
    id=photo
    print(photo)
    comments=Comments.objects.all().filter(image=id)
    return render(request, 'user/photodetails.html', {"title": title, "images":photo, "comments":comments, "id":id})

@login_required
def add_comment(request, id):
    '''
    function for adding comment to image
    '''
    title="add comments"
    
    try: 
        photo=get_object_or_404(Photos, id=id)
        print(photo)
        if request.method=='POST':
            current_user=request.user
            form=CommentForm(request.POST, request.FILES)
            if form.is_valid():
                comment=form.save(commit=False)
                comment.image=photo
                comment.user=current_user
                comment.save()
            return redirect('/')
        else:
            form=CommentForm()

    except ValueError:
        Http404
    
    return render(request, 'user/addcomment.html', {'title':title, 'form':form, "id":id })
        


@login_required
def user_profile_edit(request):
    '''
    function for editing user profile
    '''
    current_user=request.user
    title="Instagram | Profile Edit "
    if request.method=='POST':
        current_user=request.user
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=current_user
            if Profile.objects.filter(user_id=current_user.id).exists():
                Profile.objects.filter(user_id=current_user.id).delete()
            profile.save()
            return redirect('userprofile')

    else:
        form=ProfileForm()
    return render(request, 'user/profile_edit.html', {"title":title, "form":form})

    
@login_required  
def user_upload_images(request):
    '''
    function for the form uploading images to 
    instagram
    '''
    current_user=request.user
    if Profile.objects.filter(user_id=current_user.id).exists():
        if request.method=='POST':
                current_user=request.user
                form = PhotoForm(request.POST, request.FILES)
                if form.is_valid():
                    photo=form.save(commit=False)
                    user=Profile.objects.get(user=current_user)
                    photo.profile=user
                    photo.user=current_user
                    photo.save()
                    return redirect('/')
                    
        else:
            form =PhotoForm()
        return render(request, 'user/photo.html', {"form":form})
         
    else:
        return redirect(user_profile_edit)
        
            
@login_required
def user_profile(request):
    '''
    function to display the user profile
    '''
    try:
        current_user=request.user
        current_user.id=request.user.id
        title=f'Instagram | {current_user.username}'
        profile = Profile.objects.get(user_id=current_user.id)
        images = Photos.objects.all().filter(profile__user=current_user.id)
        print(images)
        return render(request, 'user/profile.html', {"title":title,"profiles":profile, "images":images})

    except:
        return redirect('profile')
    

    
    
@login_required   
def search_username(request):
    '''
    function for users to search for other 
    users on the site
    '''
    if 'username' in request.GET and request.GET['username']:
        search_term=request.GET.get('username')
        searched_profile=Profile.find_username(search_term)
        message=f'{search_term}'

        return render(request, 'user/search_profiles.html', {"message":message, "profiles":searched_profile})

    else:
        message='No one found.Sorry'
        return render(request, 'user/search_profiles.html', {"message":message})
