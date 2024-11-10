from django.urls import include, path
from rest_framework import routers
from authors.views import AuthorAPIViewSet

router = routers.DefaultRouter()
router.register('', AuthorAPIViewSet, basename='authors')

urlpatterns = [
    path('', include(router.urls)),
]