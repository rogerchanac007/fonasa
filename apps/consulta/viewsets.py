from rest_framework.viewsets import ModelViewSet
from .models import Consulta
from .serializer import ConsultaSerializer


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer