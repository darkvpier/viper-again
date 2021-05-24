from django.db import models
from django.db.models.fields import IntegerField
from django.utils.translation import ugettext_lazy as _
from django_quill.fields import QuillField

from apps.account.models import Student
class Event(models.Model):
    title = models.CharField(_("title"), max_length=200)
    description = QuillField("add description")
    start_date = models.DateField()
    duration = IntegerField(default=1)
    price = IntegerField(default=0, blank=True, null=True)
    photo = models.ImageField(upload_to='event-images/', null=True, blank=True)
    venue = models.CharField(max_length=255)
    max_enroll = models.IntegerField(default=0)
    #platforms = models.CharField(choices=PLATFORM, max_length=10)

    def __str__(self):
        return self.title

class RegisterEvent(models.Model):
    events = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.user.username
