from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Category, Topic, Post

class TestViews(TestCase):
    
    # Test User
    def setUp(self):
        
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
    
        # Test Category
        self.category_1 = Category.objects.create(
            title = "test_category",
            topic = "test_topic",
            description = "test_description",
            image_url = "test_image")
            
        # Test Topic
        self.topic_1 = Topic.objects.create(
            title = "test_topic",
            description = "test_description",
            image = "test_image",
            category = Category(pk=1),
            created_by = self.user)
            
        # Test Post
        self.post_1 = Post.objects.create(
            title = "test_post",
            description = "test_description",
            image = "test_image",
            topic = Topic(pk=1),
            author = self.user)
        
    """
    Test correct pages are returned using right templates
    """
    
    def test_get_forum_home_page(self):
        
        page = self.client.get("/forum/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "forum_home.html")
        
    def test_get_forum_category_page(self):
        
        page = self.client.get("/forum/category/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "forum_category.html")
        
    def test_get_forum_topic_page(self):
        
        page = self.client.get("/forum/topic/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "forum_topic.html")
        
    def test_get_create_topic_page_without_user_login(self):
        
        page = self.client.get("/forum/create_topic/1")
        self.assertRedirects(page, "/accounts/login/?next=/forum/create_topic/1")    
    
    def test_get_create_topic_page(self):
        
        self.client.force_login(self.user)

        page = self.client.get("/forum/create_topic/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "topic_form.html")
        
    def test_get_edit_topic_page(self):
        
        self.client.force_login(self.user)

        page = self.client.get("/forum/edit_topic/1/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "topic_form.html")
        
    def test_get_create_post_page(self):
        
        self.client.force_login(self.user)

        page = self.client.get("/forum/create_post/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "post_form.html")
        
    def test_get_edit_post_page(self):
        
        self.client.force_login(self.user)

        page = self.client.get("/forum/edit_post/1/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "post_form.html")