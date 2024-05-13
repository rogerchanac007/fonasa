from rest_framework import routers
from .viewset import EspecialistaViewSet

router = routers.SimpleRouter()
router.register('especialista', EspecialistaViewSet)

urlpatterns = router.urls