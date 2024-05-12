from django.db import models

class Paciente(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=35)
    peso = models.IntegerField(null=True)
    estatura = models.IntegerField(null=True)
    fumador = models.BooleanField(null=True)
    fecha_alta = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.nombre