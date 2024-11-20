from django.db import models
from authors.models import Author
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.contrib.postgres.indexes import GinIndex


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    author = models.ManyToManyField(
        Author,
        related_name='books'
    )
    search_vector = SearchVectorField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        Book.objects.filter(pk=self.pk).update(search_vector=SearchVector('name', 'description'))

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            GinIndex(
                fields=['search_vector']
            ),
        ]
