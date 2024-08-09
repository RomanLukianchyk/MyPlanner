from django.db import models
from django.conf import settings


class FastNote(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return f"Fast Note for {self.user.username}" # noqa