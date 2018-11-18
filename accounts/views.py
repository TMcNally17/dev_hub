from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.forms import LoginForm, UserRegistrationForm, ProfileForm


def login(request):
    
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password"])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
                return redirect(reverse("index"))
            else:
                login_form.add_error(None, "Your username or password is incorrect.")
    else:
        login_form = LoginForm()
    
    return render(request, "login.html", {"login_form": login_form})
    
@login_required
def logout(request):
    
    auth.logout(request)
    messages.success(request, "You Have Been Successfully Logged Out.")
    
    return redirect(reverse("index"))
    
def register(request):
    
    if request.user.is_authenticated:
        return redirect(reverse("index"))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if registration_form.is_valid() and profile_form.is_valid():
            registration_form.save()
            profile_form.save()
            
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password2"])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse("profile"))
            else:
                messages.error(request, "We are unable to register your account at this time. Please try again later.")
    else:
        registration_form = UserRegistrationForm()
        profile_form = ProfileForm()
        
    return render(request, "register.html", {"registration_form": registration_form, "profile_form": profile_form})
        
@login_required()
def profile(request):
    
    return render(request, "profile.html")