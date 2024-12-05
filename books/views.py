from rest_framework import viewsets
from books.documents import BookDocument
from rest_framework.response import Response
from books.serializers import BookSerializer
from rest_framework.views import APIView
from books.models import Book
from booktracker.permissions import IsAdminOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['title', 'description', 'author']
    # filter_backends = []


class BookSearchView(APIView, LimitOffsetPagination):
    serializer_class = BookSerializer
    search_document = BookDocument

    def get(self, request):
        print('/////////QUERY')
        query = request.query_params.get('q', None)
        print(query)
        print('/////////QUERY')
        if query:
            print('SEARCH')
            search = self.search_document.search().query("multi_match", query=query, fields=['name', 'description', 'author'])
            print(search)
            print("SEARCH")
            print('RESP')
            response = search.execute()
            print(response)
            print('RESP')
            result = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(result, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        return Response({'error': 'Search query is required'}, status=400)
