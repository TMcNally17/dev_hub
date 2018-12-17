from django.db import models
from django.contrib.auth.models import User
from forum.models import Topic, Category


class Ticket(models.Model):
    
    NOT_STARTED = "Not Started"
    STARTED = "Started" 
    DONE = "Done"
    STATUSES = (
        (NOT_STARTED, "Not Started"),
        (STARTED, "Started"),
        (DONE, "Done"))
    
    title = models.CharField(max_length=150, blank=False, null=False)
    topic = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUSES, default=NOT_STARTED, blank=False, null=False)
    upvotes = models.IntegerField(default=0, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.title, self.created_by, self.date)
        
        
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        
        if Topic.objects.filter(title=self.title).exists():
            topic = Topic.objects.get(title=self.title)
            Topic.objects.filter(id=topic.id).update(
                title = self.title,
                description = self.description)
        else:
            Topic.objects.create(
                title = self.title,
                description = self.description,
                created_by = self.created_by,
                category = Category(pk=2))
            
    