from django.db import models
from datetime import date

class Tarea(models.Model):
    archivo = models.FileField()
    tema = models.CharField(max_length=45, default="Tarea", null=False, blank=False)
    comentario = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(default=date.today)
    fechaLimite = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.tema}"
