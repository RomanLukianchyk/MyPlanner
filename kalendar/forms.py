from django import forms
from kalendar.models import CalendarEvent


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['event_title', 'event_description', 'event_date', 'reminder']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'reminder': forms.DateTimeInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
        }
