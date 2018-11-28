from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Ticket


class Test_Views(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
                username="test_username",
                password="test_password"
            )
            
        self.client.force_login(self.user)
    
    def test_get_tickets_page(self):
        
        page = self.client.get("/tickets/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tickets.html")
        
    def test_get_create_ticket(self):
        
        page = self.client.get("/tickets/create/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticket_form.html")
        
    def test_get_edit_ticket(self):
        ticket = Ticket(
            title = "test_title",
            topic = "test_topic",
            description = "test_description",
            created_by = self.user)
        ticket.save()
        
        page = self.client.get("/tickets/edit/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_ticket_form.html")
        
    def test_get_upvote(self):
        
        ticket = Ticket(
            title = "test_title",
            topic = "test_topic",
            description = "test_description",
            created_by = self.user)
        ticket.save()
        
        page = self.client.get("/tickets/upvote/1")
        self.assertRedirects(page, "/tickets/")
        