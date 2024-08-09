from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'standard_name', 'custom_name', 'user', 'created_by_user')

try:
    admin.site.register(Category, CategoryAdmin)
except admin.sites.AlreadyRegistered:
    pass
