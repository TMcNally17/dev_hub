from django.test import TestCase
from django.contrib.auth.models import User
from .forms import TicketForm
from .models import Ticket


class TestTicketForm(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
            
        self.client.force_login(self.user)
    
    def test_create_ticket_form(self):
        
        ticket_form = TicketForm({
            "title": "test_title",
            "topic": "test_topic",
            "description": "test_description",
            "author": self.user
        })
        ticket_form.save()
        
        self.assertTrue(ticket_form.is_valid())
        
        
    def test_create_ticket_form_with_missing_input(self):
        
        ticket_form = TicketForm({ "title": "test" })
        
        self.assertFalse(ticket_form.is_valid())
        self.assertEqual(ticket_form.errors["topic"], ["This field is required."])
        
    def test_edit_ticket_form(self):
        
        ticket_form = TicketForm({
            "title": "test_title",
            "topic": "test_topic",
            "description": "test_description",
            "author": self.user
        })
        ticket_form.save()
        
        ticket = Ticket.objects.get(pk=1)
        ticket.title = "test_edit"
        ticket.save()
        
        self.assertEqual(ticket.title, "test_edit")
        
        