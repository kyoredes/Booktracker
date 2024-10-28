from rest_framework import viewsets
from booklist.models import Readlist
from booklist.serializers import BooklistSerializer


class BooklistAPIViewSet(viewsets.ModelViewSet):
    queryset = Readlist.objects.all()
    serializer_class = BooklistSerializer
