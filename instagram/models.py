from django.db import models
from django.contrib.auth.models import User

class Photos(models.Model):
    image=models.ImageField(upload_to='articles/')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def display_images(cls):
        images=cls.objects.all()
        return images