from django.shortcuts import render
from .models import Blog


def all_blog(request):
    
    blog_posts = Blog.objects.order_by("-date")
    
    return render(request, "blog.html", {"blog_posts": blog_posts})