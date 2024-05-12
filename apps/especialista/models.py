from django.db import models

class Especialista(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=30)
    sexo= models.CharField(max_length=10)
    cedula = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres 