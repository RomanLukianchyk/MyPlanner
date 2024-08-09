from django import forms
from kalendar.models import CalendarEvent


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['event_title', 'event_description', 'event_date', 'reminder']
