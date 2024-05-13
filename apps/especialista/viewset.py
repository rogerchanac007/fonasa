from rest_framework.viewsets import ModelViewSet
from .models import Especialista
from .serializer import EspecialistaSerializer

class EspecialistaViewSet(ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer