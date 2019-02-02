from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket
from forum.models import Topic


class TestTicket(TestCase):
    
    # Test User
    def setUp(self):
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
    
    def test_create_ticket(self):
        
        # Test to create ticket to check defaults and date work
        
        self.client.force_login(self.user)
        
        ticket = Ticket(
            title = "test_title",
            topic = "test_topic",
            description = "test_description",
            created_by = self.user
        )
        ticket.save()
        
        self.assertTrue(ticket.date)
        self.assertEqual(ticket.status, "Not Started")
        self.assertEqual(ticket.upvotes, 0)
        self.assertEqual(ticket.created_by.username, "test_username")
        
        # Test to check save() creates a Topic with same data
        topic = Topic.objects.get(id=ticket.forum_id.id)
        
        self.assertEqual(topic.title, "test_title")