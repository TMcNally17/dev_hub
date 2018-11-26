from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket


class TestModels(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
    
    def test_create_ticket(self):
        
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
        
        