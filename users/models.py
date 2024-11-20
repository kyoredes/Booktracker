from django.db import models
from django.contrib.auth.models import AbstractUser
from booklists.models import Booklist


class CustomUser(AbstractUser):
    booklist = models.ForeignKey(
        Booklist,
        related_name='booklists',
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.username}"
