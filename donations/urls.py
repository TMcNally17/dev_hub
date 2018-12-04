from django.urls import path, include
from .views import make_donation


urlpatterns = [
    path('donate', make_donation, name="donations"),
]