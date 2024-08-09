from django.contrib import admin
from .models import CalendarEvent


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date', 'reminder', 'created_at', 'last_updated')
    search_fields = ('event_title', 'event_description')
    list_filter = ('event_date', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('event_title', 'event_description', 'event_date', 'reminder')
        }),
        ('Date Information', {
            'fields': ('created_at', 'last_updated'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'last_updated')
