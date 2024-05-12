from django.db import models

class Seccion(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre