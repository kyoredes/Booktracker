from rest_framework import routers
from books.views import BookAPIViewSet
from django.urls import include, path


router = routers.DefaultRouter()
router.register('', BookAPIViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
