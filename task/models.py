from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskUser(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)


class Task(models.Model):
    TASK_STATUS = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100, null=True, blank=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=TASK_STATUS, default="pending")
    assigned_users = models.ManyToManyField(TaskUser, related_name="tasks")

    def __str__(self):
        return self.name
