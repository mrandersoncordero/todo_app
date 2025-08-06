# Django
from django.db import models
from django.contrib.auth.models import User

# Utilities
from core.base_model import BaseModel


class Projects(BaseModel):

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
