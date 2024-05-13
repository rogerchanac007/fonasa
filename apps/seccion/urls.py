from .viewsets import SeccionViewSet
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register('seccion', SeccionViewSet)

urlpatterns = router.urls