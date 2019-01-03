from django.test import TestCase
from .models import Profile, Neighbourhood
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test Profile class and its methods and functions
    '''
    def setUp(self):
        self.user = User.objects.create(id =1,username='testname')
        self.neighbourhood = Neighbourhood(name='mtaani', location='hapa', user=self.user)
        # self.neighbourhood.save_neighbourhood()
        self.profile = Profile(user=self.user, hood = self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


    def test_save_method(self):
        '''
        Function that tests whether a user's profile is being saved
        '''
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a user's profile can be deleted
        '''
        self.profile.save_profile()
        self.profile.delete_profile()

