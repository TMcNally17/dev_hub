from django.urls import path
from .views import all_tickets, create_ticket, edit_ticket, upvote


urlpatterns = [
    path("", all_tickets , name="tickets"),
    path("create/", create_ticket , name="create_ticket"),
    path("edit/<int:pk>", edit_ticket , name="edit_ticket"),
    path("upvote/<int:pk>)", upvote , name="upvote"),
]