from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Topic, Post


class TestForum(TestCase):
    
    def setUp(self):
        
        # Test User 
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
        
        self.client.force_login(self.user)
    
    def test_create_category(self):
        
        # Test to create category to check defaults and date work
        category = Category(
            title = "test_category",
            topic = "test_topic",
            description = "test_description",
            image_url = "test_image")
        category.save()
            
        self.assertEqual(category.title, "test_category")
        self.assertEqual(category.posts, 0)
        self.assertTrue(category.date)
        
    def test_create_topic(self):
        
        # Test to create topic to check defaults and date work
        topic = Topic(
            title = "test_topic_1",
            description = "test_description",
            image = "test_image",
            category = Category(pk=1),
            created_by = self.user)
        topic.save()
        
        self.assertEqual(topic.title, "test_topic_1")
        self.assertFalse(topic.locked)
        
    def test_create_post(self):
        
        # Test to create post to check defaults and date work
        post = Post(
            title = "test_post",
            description = "test_description",
            image = "test_image",
            topic = Topic(pk=1),
            author = self.user)
        post.save()
            
        self.assertEqual(post.title, "test_post")
        self.assertEqual(post.author, self.user)