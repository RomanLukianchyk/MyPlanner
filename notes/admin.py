from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'creation_date', 'last_updated')
    search_fields = ('title', 'content')
    list_filter = ('user', 'creation_date')

    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'content')
        }),
        ('Date Information', {
            'fields': ('creation_date', 'last_updated'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('creation_date', 'last_updated')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
