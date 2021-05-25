from django.urls import path
from django.urls import path

from .views import EventList

urlpatterns = [
    path('list/', EventList, name='event-list')
]