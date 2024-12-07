from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    desarrollador = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulo



