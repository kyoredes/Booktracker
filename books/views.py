from rest_framework import viewsets
from books.models import Book
from books.serializers import BookSerializer
from booktracker.permissions import IsAdminOrReadOnly


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
