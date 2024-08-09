from django.db import models
from django.conf import settings


class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_path = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    doc_type = models.CharField(max_length=50)

    def __str__(self):
        return self.title