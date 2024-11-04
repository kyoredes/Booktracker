from rest_framework import viewsets
from authors.models import Author
from authors.serializers import AuthorSerializer
from readlist.permissions import IsAdminOrReadOnly


class AuthorAPIViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]
