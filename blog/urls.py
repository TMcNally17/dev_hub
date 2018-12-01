from django.urls import path
from .views import all_blog


urlpatterns = [
    path("", all_blog , name="blog"),
]