from django.db import models
from books.models import Book


class Readlist(models.Model):
    name = models.CharField(max_length=30)
    book = models.ManyToManyField(
        Book,
        related_name='books_list',
    )
