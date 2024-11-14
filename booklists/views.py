from rest_framework import viewsets
from booklists.models import Booklist
from booklists.serializers import BooklistSerializer
from booktracker.permissions import IsOwnerOrReadOnly


class BooklistAPIViewSet(viewsets.ModelViewSet):
    queryset = Booklist.objects.all()
    serializer_class = BooklistSerializer
    permission_classes = [IsOwnerOrReadOnly]
