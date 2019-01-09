from django.shortcuts import render
from blog.models import Blog

def index(request):
    
    blog = Blog.objects.latest("date")
    
    return render(request, "index.html", {"blog": blog})