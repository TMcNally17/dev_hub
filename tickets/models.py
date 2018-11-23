from django.db import models
from django.contrib.auth.models import User


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
    created_by = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title