from django.db import models

# Managers

from .managers import AutorManager


class AutorModel(models.Model):
    """Model definition for AutorModel."""

    # TODO: Define fields here
    nombre = models.CharField(
        'Nombre', 
        max_length=50
    )
    apellido = models.CharField(
        'Apellido', 
        max_length=50
    )
    nacionalidad = models.CharField(
        'Nacionalidad', 
        max_length=30
    )
    adad = models.PositiveBigIntegerField()
    
    objects = AutorManager()
    
    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        """Unicode representation of Autor."""
        return str(self.id) + ' - ' + self.nombre + ' ' + self.apellido
