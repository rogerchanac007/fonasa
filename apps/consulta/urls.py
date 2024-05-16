from rest_framework import routers
from .viewsets import ConsultaViewSet, LiberarConsultasViewSet

router = routers.SimpleRouter()
router.register('consultas', ConsultaViewSet)
router.register('liberarConsultas', LiberarConsultasViewSet, basename="liberarConsultas")

urlpatterns = router.urls