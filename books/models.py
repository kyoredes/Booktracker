from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name
