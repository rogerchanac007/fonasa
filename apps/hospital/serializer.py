from rest_framework.serializers import ModelSerializer
from .models import Hospital

class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'