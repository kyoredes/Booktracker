from django.urls import include, path
from rest_framework import routers
from authors.views import AuthorAPIViewSet

router = routers.DefaultRouter()
router.register('', AuthorAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]