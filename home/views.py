from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Blog

def index(request):
    
    try:
        blog = Blog.objects.latest("date")
    except ObjectDoesNotExist:
        blog = False
    
    return render(request, "index.html", {"blog": blog})