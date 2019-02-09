from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestProfile(TestCase):
    
    def test_user_with_profile(self):
        
        # Test Create User with Profile
        user = User(
            username = "test_username",
            first_name = "test_first",
            last_name = "test_last",
            email = "test@example.com",
            password = "test_password")
        user.save()
        
        user.profile.forum_tag = "Here is my Tag"
        user.profile.avatar = ""
        user.save()
        
        self.assertEqual(user.username, "test_username")
        self.assertEqual(user.profile.forum_tag, "Here is my Tag")