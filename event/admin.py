from django.contrib import admin
from .models import Event, EventRequest, EventChat, EventUser

# Register your models here.
admin.site.register(Event)
admin.site.register(EventUser)
admin.site.register(EventRequest)
admin.site.register(EventChat)
