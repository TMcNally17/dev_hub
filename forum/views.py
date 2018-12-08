from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Topic, Post


def forum(request):
    
    categories = Category.objects.all()
    
    return render(request, "forum_home.html", {"categories": categories})
    
def category(request, id):

    topics = Topic.objects.filter(category=id)
    
    return render(request, "forum_category.html", {"topics": topics})
    
def topic(request, id):
    
    posts = Post.objects.filter(topic=id)
    
    return render(request, "forum_topic.html", {"posts": posts})
    
@login_required
def upvote(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    post.upvotes += 1
    post.save()
    
    return redirect(reverse("topic"))