from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class LoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
        
    class Meta:
        
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        help_texts = {
            "username": ("Must be unique. No special characters only @/./+/-/_")
        }
        
    def clean_name(self):
        
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        if not first_name  or not last_name :
            raise forms.ValidationError("Please enter your name.")
        return first_name, last_name
    
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address must be unique.")
        return email
        
    def clean_password_confirm(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password.")
            
        if password1 != password2:
            raise forms.ValidationError("Passwords must match.")
            
        return password2
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["forum_tag", "avatar"]