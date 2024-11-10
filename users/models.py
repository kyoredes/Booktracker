from django.db import models
from django.contrib.auth.models import AbstractUser
from booklist.models import Booklist


class CustomUser(AbstractUser):
    booklist = models.ManyToManyField(
        Booklist,
        related_name='lists',
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.username}"
