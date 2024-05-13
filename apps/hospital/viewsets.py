from rest_framework.viewsets import ModelViewSet
from .serializer  import HospitalSerializer
from .models import Hospital

class HospitalViewSet(ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
