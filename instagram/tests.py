from django.test import TestCase
from .models import Photos, Profile, User
from django.contrib.auth.models import User



class ProfileTestClass(TestCase):
    '''
    method to test the profile class
    '''
    def setUp(self):
        '''
        method to setup and create an instance of a profile
        '''
        user= User(username="kiptim54", email="kiptim54", password="ghjkl56789dfghj")
        user.save()
        self.new_profile=Profile(profile_photo="/media/article/Screenshot_from_2018-04-15_14-56-34_LFiKDPR.png",bio="Hey there welcome to my page", user=user)
        self.new_profile.save_profile()
    def test_instance(self):
        '''
        test to see if setup is an instance of profile
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))  

    def test_deleteprofile(self):
        self.new_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    def tearDown(self):
        '''
        method to get rid of set instances
        '''
        Profile.objects.all().delete()

