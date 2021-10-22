from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(maxlength=100)
    priority=models.IntegerField()

