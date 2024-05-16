from rest_framework.serializers import ModelSerializer
from .models import Paciente

class PacienteSerializer(ModelSerializer):
    class Meta:
        model =  Paciente
        fields = '__all__'

    def create(self, validated_data):
        paciente = Paciente.objects.create(**validated_data)
        self.definirPrioridad(paciente)
        self.definirRiesgo(paciente)
        paciente.save()
        return paciente
    
    def update(self, instance, validated_data):
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.edad = validated_data.get('edad', instance.edad)
        instance.sexo = validated_data.get('sexo', instance.sexo)
        instance.domicilio = validated_data.get('domicilio', instance.domicilio)
        instance.peso = validated_data.get('peso', instance.peso)
        instance.estatura = validated_data.get('estatura', instance.estatura)
        instance.fumador = validated_data.get('fumador', instance.fumador)
        instance.años_fumando = validated_data.get('años_fumando', instance.años_fumando)
        instance.dieta = validated_data.get('dieta', instance.dieta)
        instance.fecha_alta = validated_data.get('fecha_alta', instance.fecha_alta)
        instance.no_historia_clinica = validated_data.get('no_historia_clinica', instance.no_historia_clinica)
        instance.consulta = validated_data.get('consulta', instance.consulta)
        self.definirPrioridad(instance)
        self.definirRiesgo(instance)
        instance.save()
        
        return instance
    
    def definirRiesgo(self, paciente):
        if paciente.edad >= 1 and paciente.edad <= 40:
            paciente.riesgo = (paciente.edad * paciente.prioridad)/ 100
        else:
            paciente.riesgo = (paciente.edad * paciente.prioridad)/ 100 + 5
    
    def definirPrioridad(self, paciente):
        edad = paciente.edad
        peso = paciente.peso
        estatura = paciente.estatura
        fumador = paciente.fumador
        dieta = paciente.dieta
        años_fumando = paciente.años_fumando
        prioridad = 0
        if edad >= 1 and edad <= 5:
            prioridad = peso + estatura + 3
        elif edad >= 6 and edad <= 12:
            prioridad = peso + estatura + 2
        elif edad >= 13 and edad <= 15:
            prioridad = peso + estatura + 1
        elif edad >= 16 and edad <= 40:
            if fumador:
                prioridad = años_fumando / 4 + 2
            else:
                prioridad = 2
        elif edad > 40:
            if dieta and edad >= 60 and edad <= 100:
                prioridad = edad / 20 + 4
            else:
                prioridad = edad / 30 + 3
        paciente.prioridad = prioridad

class PacienteMayorRiesgoSerializer(ModelSerializer):
    class Meta:
        model =  Paciente
        fields = '__all__'