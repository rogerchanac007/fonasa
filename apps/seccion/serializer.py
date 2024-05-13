from rest_framework.serializers import ModelSerializer
from .models import Seccion

class SeccionSerializer(ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'