from .viewsets import PacienteViewSet, PacienteMayorRiesgoViewSet, PacienteFumadorUrgente, PacienteMasAncianoViewSet, ConsultaPacientesMasAtendidos, AtenderPacientePorPrioridad
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register("pacientes", PacienteViewSet)
router.register("pacientesMayorRiesgo", PacienteMayorRiesgoViewSet, basename="pacientesMayorRiesgo")
router.register("PacienteFumadorUrgente", PacienteFumadorUrgente, basename="PacienteFumadorUrgente")
router.register("PacienteMasAnciano", PacienteMasAncianoViewSet, basename="PacienteMasAnciano")
router.register('ConsultaPacientesMasAtendidos', ConsultaPacientesMasAtendidos, basename="ConsultaPacientesMasAtendidos")
router.register('AtenderPacientePorPrioridad', AtenderPacientePorPrioridad, basename="AtenderPacientePorPrioridad")

urlpatterns = router.urls