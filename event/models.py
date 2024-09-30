from django.db import models
from django.contrib.auth.models import User
from .constants import EventRequestStatus, EventStatus, EventCategory
from base.models import AbstractBase
from django.utils import timezone

# Create your models here.

class Event(AbstractBase):
    name = models.CharField('event name', max_length=32, blank=False, null=False)
    description = models.CharField('description', max_length=64, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='events', through='EventUser', null=True, blank=True)
    limit = models.PositiveIntegerField(default=1)
    event_status = models.CharField('event status', max_length=16, choices=EventStatus, default='OPEN')
    is_private = models.BooleanField(default=False)
    starts_at = models.DateTimeField('starts on', default=timezone.now)
    category = models.CharField(max_length=32, choices=EventCategory, blank=False, null=False)
    venue = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    owner = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} is user for {self.event.name}'

class EventRequest(AbstractBase):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField('status', max_length=16, choices=EventRequestStatus, default='REQUESTED')

class EventChat(AbstractBase):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    chat = models.CharField(max_length=256, blank=False, null=False)
    replied_to = models.OneToOneField('self', blank=False, on_delete=models.CASCADE, null=False)
    messaged_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
