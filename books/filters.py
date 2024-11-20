from django_filters import rest_framework as filters
from books.models import Book


class SearchBookFilter(filters.FilterSet):
    search = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['search']
