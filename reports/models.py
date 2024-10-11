from django.db import models


class ReportTemplate(models.Model):
    name = models.CharField(max_length=100)
    template = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
