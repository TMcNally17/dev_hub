from django.urls import path
from .views import all_tickets, create_ticket


urlpatterns = [
    path("", all_tickets , name="tickets"),
    path("create/", create_ticket , name="create_ticket"),
]