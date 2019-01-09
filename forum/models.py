from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    
    title = models.CharField(max_length=150, blank=False, null=False)
    topic = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    posts = models.IntegerField(default=0, blank=False, null=False)
    image_url = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        
        return "{0}, {1}, {2}".format(self.title, self.topic, self.date)
        
class Topic(models.Model):
    
    
    title = models.CharField(unique=True, max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="forum_img", blank=True, null=True)
    posts = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    locked = models.BooleanField(default=False)
    
    def __str__(self):
        
        return "{0}, {1}, {2}".format(self.title, self.date, self.created_by)
        
class Post(models.Model):
    
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="forum_img", blank=True, null=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name="topic")
    upvotes = models.IntegerField(default=0, blank=False, null=False)
    locked = models.BooleanField(default=False)
    
    def __str__(self):
        
        return "{0}, {1}, {2}".format(self.title, self.date, self.author)