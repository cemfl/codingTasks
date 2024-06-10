# task_manager/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Task(models.Model):
    # This stores the data for each field using Django's models.
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Shows the title of the task.
        return self.title

class CustomUser(AbstractUser):
    # Remove the age field
    pass
