from django.db import models
from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    author = models.ManyToManyField(
        Author,
        related_name='books'
    )

    def __str__(self):
        return self.name
