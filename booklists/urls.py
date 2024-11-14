from django.urls import path, include
from rest_framework import routers
from booklists.views import BooklistAPIViewSet

router = routers.DefaultRouter()
router.register('', BooklistAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
