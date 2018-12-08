from django.urls import path
from .views import forum, category, topic


urlpatterns = [
    path("", forum , name="forum"),
    path("category/<id>", category , name="category"),
    path("topic/<id>", topic , name="topic"),
]