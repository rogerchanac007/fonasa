from django.db import models
from apps.consulta.models import Consulta

class Paciente(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=35)
    peso = models.IntegerField(null=True)
    estatura = models.IntegerField(null=True)
    fumador = models.BooleanField(null=True, default=False)
    años_fumando = models.IntegerField(null=True, default=0)
    dieta = models.BooleanField(null=True, default=False)
    fecha_alta = models.DateTimeField(auto_now = True)
    prioridad = models.IntegerField(null=True)
    riesgo = models.IntegerField(null=True)
    no_historia_clinica = models.IntegerField(null=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres