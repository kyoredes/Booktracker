from rest_framework import viewsets
from books.models import Book
from books.serializers import BookSerializer
from booktracker.permissions import IsAdminOrReadOnly
from books.filters import SearchBookFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchBookFilter
