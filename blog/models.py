from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    
    title = models.CharField(max_length=150, blank=False, null=False)
    topic = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_img")
    author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title