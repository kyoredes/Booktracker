from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from books.models import Book


@registry.register_document
class BookDocument(Document):
    name = fields.TextField()
    description = fields.TextField()
    author = fields.KeywordField(multi=True)

    @property
    def pk(self):
        return self.meta.id

    class Index:
        name = 'books'

    class Django:
        model = Book
        fields = ['id']

    def prepare_author(self, instance):
        return list(instance.author.values_list('first_name', 'last_name'))
