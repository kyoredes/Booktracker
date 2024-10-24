from django.db import models
from books.models import Book


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    pen_name = models.CharField(max_length=40)
    book = models.ManyToManyField(
        Book,
        related_name='authors',
    )
