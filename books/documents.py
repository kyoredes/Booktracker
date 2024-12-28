from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from books.models import Book


@registry.register_document
class BookDocument(Document):
    name = fields.TextField()
    description = fields.TextField()
    author = fields.ObjectField(
        properties={
            "first_name": fields.TextField(),
            "last_name": fields.TextField(),
        }
    )

    class Index:
        name = "books"

    class Django:
        model = Book
        fields = ["id"]

    def prepare_authors(self, instance):
        return [
            {
                "id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,
            }
            for author in instance.authors.all()
        ]
