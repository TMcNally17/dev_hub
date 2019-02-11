from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestViews(TestCase):
    
    # Test User
    def setUp(self):
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
    
    """
    Test correct pages are returned using right templates
    """
    
    def test_get_register_page(self):
        
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")
        
    def test_get_login_page(self):
        
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    def test_get_profile_page(self):
        
        self.client.force_login(self.user)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    def test_get_profile_without_user_login(self):
        
        page = self.client.get("/accounts/profile/")
        self.assertRedirects(page, "/accounts/login/?next=/accounts/profile/")
        
    def test_get_edit_profile_page(self):
        
        self.client.force_login(self.user)
        page = self.client.get("/accounts/profile/edit")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_profile.html")
        
    def test_get_edit_profile_without_user_login(self):
        
        page = self.client.get("/accounts/profile/edit")
        self.assertRedirects(page, "/accounts/login/?next=/accounts/profile/edit")