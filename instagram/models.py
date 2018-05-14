from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='article/')
    bio=models.CharField(max_length=100)
    user=models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE )
    name=models.CharField(max_length=50)
    # follows=models.ManyToManyField()
    # username=models.CharField(max_length=50)
    
    def save_profile(self):
        self.save()
        return self.save()

    @classmethod
    def display_profile(cls):
        print("hello")
        profiles=cls.objects.get(pk=1)
        print(profiles)
        return profiles

    def delete_profile(self):
        return self.delete()
    
    @classmethod
    def find_username(cls, search_term):
        profiles=cls.objects.filter(name__icontains=search_term)
        return profiles

        
    def __str__(self):
        return self.user.username


class Photos(models.Model):
    image=models.ImageField(upload_to='articles/')
    image_name=models.CharField(blank=True, max_length=50)
    image_caption=models.CharField(blank=True,max_length=200)
    profile=models.ForeignKey(Profile, related_name="user_profile")
    posted= models.DateTimeField(auto_now_add=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True, null=True)
    # likes=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    

    def __str__(self):
        return self.image_name
   

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def display_images(cls):
        images=cls.objects.all() 
        return images

  
class Comments(models.Model):
    comment=models.TextField(blank=True, max_length=300) 
    posted = models.DateTimeField(auto_now_add=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ForeignKey(Photos)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def display_comments(cls):
        comments=cls.objects.all()
        return comments

    @classmethod
    def comment_byphoto(cls, id):
        comment=cls.objects.filter(image=id)
        return comment

class Likes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_likes(cls):
        likes=cls.objects.all()
        return likes



