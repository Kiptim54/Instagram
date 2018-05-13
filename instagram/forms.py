from .models import Photos , Profile, Comments
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name', 'bio', 'profile_photo']

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photos
        fields=['image', 'image_name', 'image_caption']    

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comment']    