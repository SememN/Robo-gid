from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=60)
    preview = models.TextField(max_length=300)
    description = models.TextField(max_length=5000)
    teacher = models.TextField(max_length=60)
