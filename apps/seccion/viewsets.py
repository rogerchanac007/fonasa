from rest_framework.viewsets import ModelViewSet
from .serializer import SeccionSerializer
from .models import Seccion

class SeccionViewSet(ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer