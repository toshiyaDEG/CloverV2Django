from django.db import models

class Materia(models.Model):
    MATERIA = [
        ("LM", "Lengua Materna"),
        ("DM", "Desafíos Matemáticos"),
        ("CN", "Ciencias Naturales"),
        ("ECE", "Educación cívica y ética"),
        ("J", "Jalisco"),
        ("EF", "Educación física"),
    ]
    materia = models.CharField(max_length=3, choices=MATERIA, default="LM")

    def __str__(self):
        """ Representación en str para usar Materia """
        return self.materia
