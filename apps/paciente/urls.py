from .viewsets import PacienteViewSet
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register("pacientes", PacienteViewSet)

urlpatterns = router.urls