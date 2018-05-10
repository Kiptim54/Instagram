from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='article/')
    bio=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE )


class Photos(models.Model):
    image=models.ImageField(upload_to='articles/')
    image_name=models.CharField(blank=True, max_length=50)
    image_caption=models.CharField(blank=True,max_length=100)
    profile=models.ForeignKey(Profile)
   

    @classmethod
    def display_images(cls):
        images=cls.objects.all()
        return images