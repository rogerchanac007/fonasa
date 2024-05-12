from django.db import models

class Hospital(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    

    def __str__(self):
        return self.nombre
