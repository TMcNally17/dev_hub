from django.test import TestCase
from django.contrib.auth.models import User
from .forms import NewTopicForm, EditTopicForm, PostForm
from .models import Category, Topic, Post


class TestForumForms(TestCase):
    
    # Test User
    def setUp(self):
        
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
            
        self.client.force_login(self.user)
        
    def test_create_topic_form(self):
        
        # Test topic form is valid with correct inputs
        topic_form = NewTopicForm({
            "title": "test_topic",
            "description": "test_description",
            "image": "test_image"})
        topic_form.save()
        
        self.assertTrue(topic_form.is_valid())
        
    def test_topic_form_with_same_title(self):
        
        # Test topic with same name as one that exists is not validated
        topic_form = NewTopicForm({
            "title": "test_topic",
            "description": "test_description",
            "image": "test_image"})
        topic_form.save()
        
        topic_form_1 = NewTopicForm({
            "title": "test_topic",
            "description": "test_description_1",
            "image": "test_image_1"})

        self.assertFalse(topic_form_1.is_valid())
        self.assertEqual(topic_form_1.errors["title"], ["Please use another title. This one already exists."])
        
    def test_edit_topic_form(self):
        
        # Test topic form is updated with different data
        topic_form = EditTopicForm({
            "title": "test_title",
            "description": "test_description",
            "image": "test_image"})
        topic_form.save()
        
        topic = Topic.objects.get(id=1)
        topic.title = "test_edit"
        topic.save()
        
        self.assertEqual(topic.title, "test_edit")
       
    def test_create_post_form(self):
        
        # Test post form is valid with correct inputs
        post_form = PostForm({
            "title": "test_post",
            "description": "test_description",
            "image": "test_image"})
        post_form.save()
        
        self.assertTrue(post_form.is_valid())
        
    def test_edit_post_form(self):
        
        # Test post form is updated with different data
        post_form = PostForm({
            "title": "test_title",
            "description": "test_description",
            "image": "test_image"})
        post_form.save()
        
        post = Post.objects.get(id=1)
        post.title = "test_edit"
        post.save()
        
        self.assertEqual(post.title, "test_edit")