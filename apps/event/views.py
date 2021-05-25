
from apps.event.forms import EventForm
from django.shortcuts import render

from apps.event.models import Event


# Create your views here.
def EventList(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render( request, 'events/event-list.html', context)

