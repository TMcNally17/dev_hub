from django.test import TestCase
from django.contrib.auth.models import User
from .forms import TopicForm, PostForm
from .models import Category, Topic, Post


class TestForumForms(TestCase):
    
    # Test User
    def setUp(self):
        
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
            
        self.client.force_login(self.user)
        
    def test_topic_form(self):
        
        # Test topic form is valid with correct inputs
        topic_form = TopicForm({
            "title": "test_topic",
            "description": "test_description",
            "image": "test_image"})
        topic_form.save()
        
        self.assertTrue(topic_form.is_valid())
    
    def test_post_form(self):
        
        # Test post form is valid with correct inputs
        post_form = PostForm({
            "title": "test_post",
            "description": "test_description",
            "image": "test_image"})
        post_form.save()
        
        self.assertTrue(post_form.is_valid())