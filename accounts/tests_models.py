from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestProfile(TestCase):
    
    def test_user_with_profile(self):
        
        user = User(
            username = "test_username",
            first_name = "test_first",
            last_name = "test_last",
            email = "test@example.com",
            password = "test_password")
        user.save()
        profile = Profile(
            user.id,
            forum_tag = "Here is my Tag",
            avatar = "")
        user.profile = profile
        user.save()
        
        self.assertEqual(user.username, "test_username")
        self.assertEqual(user.profile.forum_tag, "Here is my Tag")