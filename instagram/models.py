from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='article/')
    bio=models.CharField(max_length=100)
    user=models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE )
    # follows=models.ManyToManyField()
    # username=models.CharField(max_length=50)
    
    def save_profile(self):
        return self.save()
    
    def delete_profile(self):
        return self.delete()
    
    @classmethod
    def find_profilename(cls, search_term):
        cls.objects.filyer(user__iexact=search_term)

        
    def __str__(self):
        return self.bio

    
    



class Photos(models.Model):
    image=models.ImageField(upload_to='articles/')
    image_name=models.CharField(blank=True, max_length=50)
    image_caption=models.CharField(blank=True,max_length=200)
    profile=models.ForeignKey(Profile, related_name="user_profile")
    likes=models.IntegerField(blank=True)
    comment=models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.image
   

    def save_photo(self):
        self.save()

    @classmethod
    def display_images(cls):
        images=cls.objects.all()
        return images

    