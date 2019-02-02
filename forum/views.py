from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Topic, Post
from .forms import TopicForm, PostForm


def forum(request):
    
    categories = Category.objects.order_by("id")
    
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
    
def category(request, category_id):
    
    category = Category.objects.get(id=category_id)
    topics = Topic.objects.filter(category=category_id)
    
    total_posts = 0
    for topic in topics:
        posts = Post.objects.filter(topic=topic.id).count()
        total_posts += posts
    
    category.posts = total_posts
    category.save()
    
    return render(request, "forum_category.html", {"category": category,
                                                    "topics": topics, 
                                                    "category_id": category_id})
    
def topic(request, topic_id):
    
    topic = Topic.objects.get(id=topic_id)
    posts = Post.objects.filter(topic=topic_id)
    category_id = topic.category.id
    
    posts_count = Post.objects.filter(topic=topic.id).count()
    topic.posts = posts_count
    topic.save()
    
    return render(request, "forum_topic.html", {"posts": posts,
                                                "topic": topic,
                                                "category_id": category_id,
                                                "topic_id": topic_id})
    
@login_required
def create_topic(request, category_id):
    
    context = "Create Topic"
    if request.method == "POST":
        
        topic_form = TopicForm(request.POST, request.FILES)
        
        if topic_form.is_valid():
            topic = topic_form.save()
            topic.created_by = request.user
            topic.category = Category(pk=category_id)
            topic.save()
            messages.success(request, "Topic was successfully posted.")
            
            return redirect(reverse("category", kwargs={"category_id": category_id}))
    else:
        topic_form = TopicForm()
    
    return render(request, "topic_form.html", {"topic_form": topic_form, 
                                                "context": context})
    
@login_required
def edit_topic(request, category_id, topic_id):
    
    context = "Edit Topic"
    
    topic = Topic.objects.get(id=topic_id)
    topic_title = topic.title
    if request.user == topic.created_by or request.user.is_staff:
        
        if request.method == "POST":
            topic_form = TopicForm(request.POST, request.FILES, instance=Topic.objects.get(id=topic_id))
            
            if topic_form.is_valid():
                topic_form.save()
                messages.success(request, "Topic was successfully edited.")
                return redirect(reverse("category", kwargs={"category_id": category_id})) 
        else:
            topic_form = TopicForm(instance=Topic.objects.get(id=topic_id))
    else:
        return redirect(reverse("category", kwargs={"category_id": category_id}))
    
    return render(request, "topic_form.html", {"topic_form": topic_form,
                                                "context": context,
                                                "topic_title": topic_title})
    
@login_required
def create_post(request, topic_id):
    
    context = "Create Post"
    topic = Topic.objects.get(id=topic_id)
    
    if request.method == "POST":
        
        post_form = PostForm(request.POST, request.FILES)
        
        if post_form.is_valid():
            post = post_form.save()
            post.author = request.user
            post.topic = Topic(pk=topic_id)
            post.save()
            messages.success(request, "Post was successfully posted.")
            
            return redirect(reverse("topic", kwargs={"topic_id": topic_id}))
    else:
        post_form = PostForm()
            
    return render(request, "post_form.html", {"post_form": post_form,
                                            "topic": topic,
                                            "context": context,
                                            "topic_id": topic_id})
    
@login_required
def edit_post(request, topic_id, post_id):
    
    context = "Edit Post"
    topic = Topic.objects.get(id=topic_id)
    
    post = Post.objects.get(id=post_id)
    if request.user == post.author or request.user.is_staff():
    
        if request.method == "POST":
            post_form = PostForm(request.POST, request.FILES, instance=Post.objects.get(id=post_id))
            
            if post_form.is_valid():
                post_form.save()
                messages.success(request, "Post was successfully edited.")
                return redirect(reverse("topic", kwargs={"topic_id": topic_id})) 
        else:
            post_form = PostForm(instance=Post.objects.get(id=post_id))
    else:
         return redirect(reverse("topic", kwargs={"topic_id": topic_id}))
    
    return render(request, "post_form.html", {"post_form": post_form,
                                                "topic": topic,
                                                "context": context,
                                                "topic_id": topic_id})
    
@login_required
def upvote_post(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    post.upvotes += 1
    post.save()
    messages.success(request, "Thank you for upvoting.")
    
    return redirect(reverse("topic", kwargs={"topic_id": post.topic.id}))