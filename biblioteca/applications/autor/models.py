from django.db import models

# Managers

from .managers import AutorManager


class Personas(models.Model):
    
    nombres = models.CharField(
        'Nombre', 
        max_length=50
    )
    apellidos = models.CharField(
        'Apellido',
        max_length=50
    )
    nacionalidad = models.CharField(
        'Nacionalidad', 
        max_length=20
    )
    edad = models.PositiveIntegerField(default=0)


    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        abstract = True

    def __str__(self):
        """Unicode representation of Autor."""
        return str(self.id) + ' - ' + self.nombres + ' ' + self.apellidos



class AutorModel(Personas):
    seudonimo = models.CharField(
        'Suedonimo', 
        max_length = 50,
        blank = True
    )
    objects = AutorManager()
