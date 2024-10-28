from rest_framework import routers
from users import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', views.UserAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
