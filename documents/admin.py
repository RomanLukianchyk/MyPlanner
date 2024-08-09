from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'upload_date', 'doc_type')
    search_fields = ('title', 'user__username', 'doc_type')
    list_filter = ('upload_date', 'doc_type')
