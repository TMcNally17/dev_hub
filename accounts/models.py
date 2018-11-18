from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forum_tag = models.TextField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="images", blank=True)
    
