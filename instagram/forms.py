from .models import Photos
from django import forms

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photos
        exclude=['profile']