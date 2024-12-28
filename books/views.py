from rest_framework import viewsets
from books.documents import BookDocument
from rest_framework.response import Response
from books.serializers import BookSearchSerializer, BookSerializer
from rest_framework.views import APIView
from books.models import Book
from booktracker.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    search_fields = ["title", "description", "author"]
    # filter_backends = []


class BookSearchView(APIView, LimitOffsetPagination):
    serializer_class = BookSearchSerializer
    search_document = BookDocument

    def get(self, request):
        query = request.query_params.get("q", None)
        if query:

            search = self.search_document.search().query(
                "multi_match",
                query=query,
                fields=["name", "description", "author"],
            )

            response = search.execute()

            hits = [
                {
                    "id": hit.meta.id,
                    "name": hit.name,
                    "description": hit.description,
                    "author": hit.author,
                }
                for hit in response
            ]
            result = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(
                result, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)
        return Response({"error": "Search query is required"}, status=400)
