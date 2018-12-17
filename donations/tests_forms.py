from django.test import TestCase
from django.contrib.auth.models import User
from .forms import DonationForm
from .models import Donation


class TestDonationForms(TestCase):
    
    # Test User
    def setUp(self):
        
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
            
        self.client.force_login(self.user)
    
    def test_donation_form(self):
        
        # Test donation form is valid with correct inputs
        donation_form = DonationForm({
            "first_name": "test_first",
            "last_name": "test_last",
            "email": "test@example.com",
            "donation_amount": 10})
        donation_form.save()
        
        donation = Donation.objects.get(id=1)
        
        self.assertTrue(donation_form.is_valid())
        self.assertEqual(donation.email, "test@example.com")
    
    def test_donation_form_with_missing_inputs(self):
        
        # Test donation form is invalid with missing inputs
        donation_form = DonationForm({
            "first_name": "test_first",
            "last_name": "test_last",
            "email": "",
            "donation_amount": 10})
        
        self.assertFalse(donation_form.is_valid())
        self.assertEqual(donation_form.errors["email"], ["This field is required."])