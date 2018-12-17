from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import LoginForm, UserRegistrationForm, ProfileForm


class TestUserForms(TestCase):
    
    # Test LoginForm
    
    def test_login_form(self):
        
        form = LoginForm({"username": "test", "password": "testpassword"})
        
        self.assertTrue(form.is_valid())
        
    def test_login_form_missing_input(self):
        
        form = LoginForm({"username": "test", "password": " "})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password"], ["This field is required."])
    
    """
    Test UserRegistrationForm
    """
    
    def test_user_registration_form(self):
        
        # Test User Registration Form is valid with correct inputs
        user_form = UserRegistrationForm({
            "username": "test_username",
            "first_name": "test_first",
            "last_name": "test_last",
            "email": "test@example.com",
            "password1": "test_password",
            "password2": "test_password"
        })
        
        self.assertTrue(user_form.is_valid())
        user_form.save()
        
        user = get_object_or_404(User, pk=1)
        self.assertEqual(user.username, "test_username")
        
    def test_user_registration_form_with_same_email(self):
        
        # Test User Registration Form is not valid when email is not unique 
        user_form_1 = UserRegistrationForm({
            "username": "test_username",
            "first_name": "test_first",
            "last_name": "test_last",
            "email": "test@example.com",
            "password1": "test_password",
            "password2": "test_password"})
            
        user_form_1.save()
        
        user_form_2 = UserRegistrationForm({
            "username": "tes1_username",
            "first_name": "test1_first",
            "last_name": "test1_last",
            "email": "test@example.com",
            "password1": "test1_password",
            "password2": "test1_password"})
            
        self.assertFalse(user_form_2.is_valid())
        self.assertEqual(user_form_2.errors["email"], ["Email address must be unique."])
    
    def test_correct_error_missing_input(self):
        
        # Test User Registration Form is not valid with missing inputs
        form = UserRegistrationForm({"username": " "})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], ["This field is required."])
        
    def test_passwords_do_not_match(self):
        
        # Test User Registration Form is not valid with not matching passwords
        user_form = UserRegistrationForm({
            "username": "test_username",
            "first_name": "test_first",
            "last_name": "test_last",
            "email": "test@example.com",
            "password1": "test_password",
            "password2": "not_test_password"})
            
        self.assertFalse(user_form.is_valid())
        self.assertNotEqual(user_form["password1"], user_form["password2"])