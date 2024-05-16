from django.db import models
from ..hospital.models import Hospital
from ..especialista.models import Especialista

STATUS = {
    1:'Pendiente',
    2:'Ocupada',
    3:'Finalizada'
}

class Consulta(models.Model):
    fecha = models.DateTimeField(null=True)
    fecha_modificado = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=STATUS[1])
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
