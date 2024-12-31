from celery import shared_task
from elasticsearch import Elasticsearch
from books.models import Book

es = Elasticsearch(
    hosts=[
        "http://elasticsearch:9200",
    ]
)


@shared_task
def update_index(book_id):
    try:
        book_object = Book.objects.all().filter(id=book_id)
        es.index(
            index="books",
            id=book_id,
            body={
                "name": book_object.name,
                "description": book_object.description,
                "author": book_object.author,
            },
        )
        return f"Book index {book_id} added"
    except Book.DoesNotExist:
        return f"Book {book_id} does not exist"
