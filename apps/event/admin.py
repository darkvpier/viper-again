from django.contrib import admin
from .models import  Event, RegisterEvent

admin.site.register(Event)
admin.site.register(RegisterEvent)