from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count, Q, Sum
from .forms import LoginForm, UserRegistrationForm, ProfileForm
from forum.models import Post, Topic
from tickets.models import Ticket



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
        
        if registration_form.is_valid():
            registration_form.save()
            
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
        
    return render(request, "register.html", {"registration_form": registration_form})
    
@login_required()
def profile(request):
    
    posts = Post.objects.filter(author=request.user).count()
    topics = Topic.objects.filter(created_by=request.user).count()
    tickets = Ticket.objects.filter(created_by=request.user).order_by("date")
    
    return render(request, "profile.html", {"posts": posts,
                                            "topics": topics,
                                            "tickets": tickets})
        
@login_required()
def edit_profile(request):
 
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ("Your profile was successfully updated."))
            return redirect(reverse("profile"))
        else:
            messages.error(request, ("We can't change your profile at this time. Try again later."))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        
    return render(request, "edit_profile.html", {"profile_form": profile_form})