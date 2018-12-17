from django.urls import path
from .views import all_tickets, create_ticket, edit_ticket, upvote_ticket


urlpatterns = [
    path("", all_tickets , name="tickets"),
    path("create/", create_ticket , name="create_ticket"),
    path("edit/<id>", edit_ticket , name="edit_ticket"),
    path("upvote/<id>", upvote_ticket , name="upvote_ticket"),
]