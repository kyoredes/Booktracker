from rest_framework import viewsets
from booklist.models import Booklist
from booklist.serializers import BooklistSerializer
from booktracker.permissions import IsOwnerOrReadOnly


class BooklistAPIViewSet(viewsets.ModelViewSet):
    queryset = Booklist.objects.all()
    serializer_class = BooklistSerializer
    permission_classes = [IsOwnerOrReadOnly]
