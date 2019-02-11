from django.db import models
from django.contrib.auth.models import User
from forum.models import Topic, Category


class Blog(models.Model):
    
    title = models.CharField(unique=True, max_length=150, blank=False, null=False)
    topic = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    image = models.CharField(max_length=50, null=True)
    forum_id = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.title, self.date, self.author)
    
    def save(self, *args, **kwargs):
        try:
            Topic.objects.filter(id=self.forum_id.id).update(
                title = self.title,
                description = self.description)
        except:
            topic = Topic.objects.create(
                title = self.title,
                description = self.description,
                created_by = self.author,
                category = Category(pk=3))
            self.forum_id = Topic(pk=topic.id)
        
        super().save(*args, **kwargs)