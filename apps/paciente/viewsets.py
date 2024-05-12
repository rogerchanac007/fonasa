from rest_framework.viewsets import ModelViewSet
from .serializer import PacienteSerializer
from .models import Paciente

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer