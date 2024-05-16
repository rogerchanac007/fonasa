from rest_framework.viewsets import ModelViewSet
from .serializer import PacienteSerializer
from apps.consulta.serializer import ConsultaSerializer
from .models import Paciente
from apps.consulta.models import Consulta
from django.db.models import F, Q, Count


class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteMayorRiesgoViewSet(ModelViewSet):
    queryset = Paciente.objects.filter(prioridad__gt=F('no_historia_clinica'))
    serializer_class = PacienteSerializer

class PacienteFumadorUrgente(ModelViewSet):
    queryset = Paciente.objects.filter(Q(fumador=True), prioridad__lte=4)
    serializer_class = PacienteSerializer

class PacienteMasAncianoViewSet(ModelViewSet):
    queryset = Paciente.objects.order_by("-edad")[:1]
    serializer_class = PacienteSerializer

class ConsultaPacientesMasAtendidos(ModelViewSet):
    mayorConsulta = Paciente.objects.values("consulta").annotate(cuenta=Count('consulta')).order_by("-cuenta")[:1][0]["consulta"]
    queryset = Consulta.objects.filter(Q(pk=mayorConsulta))
    serializer_class = ConsultaSerializer

class AtenderPacientePorPrioridad(ModelViewSet):
    queryset = Paciente.objects.filter(Q(consulta__status=1)).order_by("-prioridad")
    serializer_class = PacienteSerializer
