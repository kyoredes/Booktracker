from rest_framework import routers
from books.views import BookAPIViewSet
from django.urls import include, path
from books.views import BookSearchView

router = routers.DefaultRouter()
router.register('', BookAPIViewSet)


urlpatterns = [
    path('search/', BookSearchView.as_view(), name='book-search'),
    path('', include(router.urls)),

]
