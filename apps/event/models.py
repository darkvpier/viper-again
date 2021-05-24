from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_quill.fields import QuillField

class Event(models.Model):
    title = models.CharField(_("title"), max_length=200)
    description = QuillField("add description")
    start_date = models.DateField()
    end_date = models.DateField(default="2021-12-12")
    photo = models.ImageField(upload_to='event-images/', null=True, blank=True)
    max_enroll = models.IntegerField(default=0)
    #platforms = models.CharField(choices=PLATFORM, max_length=10)