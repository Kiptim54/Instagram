from django.test import TestCase
from .models import Photos, Profile, User
from django.contrib.auth.models import User


def setUp(self):
        #creating new user
        user= User(username="kiptim54", email="kiptim54", password="ghjkl56789dfghj")
        user.save()
        #creating new profile
        self.new_profile=Profile(id=1 ,profile_photo="/media/article/Screenshot_from_2018-04-15_14-56-34_LFiKDPR.png",bio="Hey there welcome to my page", user=user)
        
        #creating new image
        self.new_image=Photos(id=1,image="/media/article/Screenshot_from_2018-04-15_14-56-34_LFiKDPR.png", image_name="Anything", image_caption="This life chose us", profile=self.new_profile, likes="4", comment="Nice photo you have here")
        

def tearDown(self):
        '''
        method to get rid of set instances
        '''
        Profile.objects.all().delete()
        User.objects.all().delete()

        
class ProfileTestClass(TestCase):
    '''
    method to test the profile class
    '''

    def test_savingprofile(self):
        setUp(self)
        self.new_profile=Profile
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_instance(self):
        '''
        test to see if setup is an instance of profile
        '''
        tearDown(self)
        setUp(self)
        self.assertTrue(isinstance(self.new_profile, Profile))  

    def test_deleteprofile(self):
        tearDown(self)
        setUp(self)
        self.new_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)


class PhotoTestClass(TestCase):
    '''
    method tests the Image class
    '''
    def test_saveimage(self):
        tearDown(self)
        setUp(self) 
        self.new_image.save_photo 
        images=Photos.objects.all() 
        self.assertTrue(len(images)>0) 

    def test_instance(self):
        tearDown(self)
        setUp(self)
        self.assertTrue(isinstance(self.new_image, Photos))

    def test_deletephoto(self):
        tearDown(self)
        setUp(self)
        self.new_image.delete_photo()
        images=Photos.objects.all()
        self.assertTrue(len(images)==0)


    
        