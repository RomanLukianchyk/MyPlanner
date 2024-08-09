from django.db import models
from django.conf import settings


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    standard_name = models.CharField(max_length=100, blank=True, null=True)
    custom_name = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_by_user = models.BooleanField(default=False)

    def __str__(self):
        if self.created_by_user:
            return self.custom_name
        return self.standard_name

    @classmethod
    def create_standard_categories(cls):
        standard_categories = ['study', 'work', 'leisure', 'family', 'finance', 'yearly_plans', 'monthly_plans']
        for name in standard_categories:
            cls.objects.get_or_create(standard_name=name, created_by_user=False)

    @classmethod
    def create_custom_category(cls, custom_name, user):
        cls.objects.create(custom_name=custom_name, user=user, created_by_user=True)


