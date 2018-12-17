from django.urls import path
from .views import graphs

urlpatterns = [
    path('', graphs, name="graphs")
]