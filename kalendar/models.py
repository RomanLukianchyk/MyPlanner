from django.db import models
from django.conf import settings

class CalendarEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateTimeField()
    reminder = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
