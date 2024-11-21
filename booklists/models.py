from django.db import models
from books.models import Book
from django.contrib.auth import get_user_model


class Booklist(models.Model):
    name = models.CharField(max_length=30)
    book = models.ManyToManyField(
        Book,
        related_name='books',
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
