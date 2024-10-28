from django.db import models
from django.contrib.auth.models import AbstractUser
from booklist.models import Readlist


class CustomUser(AbstractUser):
    booklist = models.ManyToManyField(
        Readlist,
        related_name='lists',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
