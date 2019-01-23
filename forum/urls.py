from django.urls import path
from .views import forum, category, topic, create_topic, edit_topic, create_post, edit_post, upvote_post


urlpatterns = [
    path("", forum , name="forum"),
    path("category/<category_id>", category , name="category"),
    path("topic/<topic_id>", topic , name="topic"),
    path("create_topic/<category_id>", create_topic , name="create_topic"),
    path("edit_topic/<category_id>/<topic_id>", edit_topic , name="edit_topic"),
    path("create_post/<topic_id>", create_post , name="create_post"),
    path("edit_post/<topic_id>/<post_id>", edit_post , name="edit_post"),
    path("upvote/<id>", upvote_post , name="upvote_post"),
]