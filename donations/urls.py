from django.urls import path, include
from .views import donations, donate


urlpatterns = [
    path('', donations, name="donations"),
    path('donate/<int:amount>', donate, name="donate"),
]