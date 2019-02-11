from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Donation

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
    
    def test_get_donation_page(self):
        
        page = self.client.get("/donations/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "donation.html")
        
    def test_get_donate_page(self):
        
        self.client.force_login(self.user)
        
        page = self.client.get("/donations/donate/500")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "donation.html")
        
    def test_get_donate_page_without_user_login(self):
        
        page = self.client.get("/donations/donate/500")
        self.assertRedirects(page, "/accounts/login/?next=/donations/donate/500")