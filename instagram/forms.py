from .models import Photos , Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name', 'bio', 'profile_photo']

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photos
        fields=['image', 'image_name', 'image_caption']        