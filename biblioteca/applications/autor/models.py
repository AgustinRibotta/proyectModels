from django.db import models

# Create your models here.


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
    
    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        """Unicode representation of Autor."""
        return self.name + ' ' + self.apellido
