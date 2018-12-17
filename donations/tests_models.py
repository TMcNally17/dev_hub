from django.test import TestCase
from django.contrib.auth.models import User
from .models import Donation


class TestForum(TestCase):
    
    
    def test_create_donation(self):
        
        # Test to create donation
        donation = Donation(
            first_name = "test_first",
            last_name = "test_last",
            email = "test@example.com",
            donation_amount = 10)
        donation.save()
        
        self.assertEqual(donation.email, "test@example.com")
        self.assertEqual(donation.donation_amount, 10)
        self.assertTrue(donation.date)