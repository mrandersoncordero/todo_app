# Django
from django.db import models

# Models
from projects.models import Projects

# Utilities
from core.base_model import BaseModel


class Tasks(BaseModel):

    class Status(models.TextChoices):
        PENDING = "pending"
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"

    class Priority(models.TextChoices):
        LOW = "low"
        MEDIUM = "medium"
        HIGH = "high"

    project = models.ForeignKey(Projects, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    priority = models.CharField(
        max_length=6, choices=Priority.choices, default=Priority.LOW
    )
    deadline = models.DateTimeField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["-deadline"]),
        ]

    def __str__(self):
        return self.title
