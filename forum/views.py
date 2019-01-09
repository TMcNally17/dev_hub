from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Topic, Post
from .forms import TopicForm, PostForm


def forum(request):
    
    categories = Category.objects.all()
    
    for category in categories:
        topics = Topic.objects.filter(category=category.id)
        total_posts = 0
        for topic in topics:
            posts = Post.objects.filter(topic=topic.id).count()
            topic.posts = posts
            topic.save()
            total_posts += posts
        
        category.posts = total_posts
        category.save()
    
    return render(request, "forum_home.html", {"categories": categories})
    
def category(request, id):

    topics = Topic.objects.filter(category=id)
    
    return render(request, "forum_category.html", {"topics": topics, "id":id})
    
def topic(request, id):
    
    topic = Topic.objects.get(id=id)
    posts = Post.objects.filter(topic=id)
    
    return render(request, "forum_topic.html", {"posts": posts, "topic": topic, "id":id})
    
@login_required
def create_topic(request, id):
    
    context = "Create Topic"
    
    if request.method == "POST":
        
        topic_form = TopicForm(request.POST)
        
        if topic_form.is_valid():
            topic = topic_form.save()
            topic.created_by = request.user
            topic.category = Category(pk=id)
            topic.save()
            messages.success(request, "Topic was successfully posted.")
            
            return redirect(reverse("category", kwargs={"id": id}))
    else:
        topic_form = TopicForm()
    
    return render(request, "topic_form.html", {"topic_form": topic_form, "context": context})
    
@login_required
def edit_topic(request, id):
    
    context = "Edit Topic"
    
    topic = Topic.objects.get(id=id)
    if request.user == topic.created_by:
        
        if request.method == "POST":
            topic_form = TopicForm(request.POST, instance=Topic.objects.get(id=id))
            
            if topic_form.is_valid():
                topic_form.save()
                messages.success(request, "Topic was successfully edited.")
                return redirect(reverse("category", kwargs={"id": topic.category})) 
        else:
            topic_form = TopicForm(instance=Topic.objects.get(id=id))
    else:
        return redirect(reverse("category", kwargs={"id": topic.category}))
    
    return render(request, "topic_form.html", {"topic_form": topic_form, "context": context})
    
@login_required
def create_post(request, id):
    
    context = "Create Post"
    topic = Topic.objects.get(id=id)
    
    if request.method == "POST":
        
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            post = post_form.save()
            post.author = request.user
            post.topic = Topic(pk=id)
            post.save()
            messages.success(request, "Post was successfully posted.")
            
            return redirect(reverse("topic", kwargs={"id": id}))
    else:
        post_form = PostForm()
            
    return render(request, "post_form.html", {"post_form": post_form, "topic": topic, "context": context})
    
@login_required
def edit_post(request, id):
    
    context = "Edit Post"
    topic = Topic.objects.get(id=id)
    
    post = Post.objects.get(id=id)
    if request.user == post.author:
    
        if request.method == "POST":
            post_form = PostForm(request.POST, instance=Post.objects.get(id=id))
            
            if post_form.is_valid():
                post_form.save()
                messages.success(request, "Post was successfully edited.")
                return redirect(reverse("category", kwargs={"id": post.topic})) 
        else:
            post_form = TopicForm(instance=Post.objects.get(id=id))
    else:
         return redirect(reverse("topic", kwargs={"id": post.topic}))
    
    return render(request, "post_form.html", {"post_form": post_form, "topic": topic, "context": context})
    
@login_required
def upvote_post(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    post.upvotes += 1
    post.save()
    
    return redirect(reverse("topic", kwargs={"id": post.topic.id}))