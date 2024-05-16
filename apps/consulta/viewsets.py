from rest_framework.viewsets import ModelViewSet
from .models import Consulta
from apps.paciente.models import Paciente
from .serializer import ConsultaSerializer
from django.db.models import Q, Count


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class LiberarConsultasViewSet(ModelViewSet):
    queryset = Consulta.objects.filter(Q(status=2))
    queryset.update(status=3)
    serializer_class = ConsultaSerializer

