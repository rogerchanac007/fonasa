from rest_framework import routers
from .viewsets import HospitalViewSet

router = routers.SimpleRouter()
router.register('hospital', HospitalViewSet)

urlpatterns = router.urls