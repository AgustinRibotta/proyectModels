from django.db import models
from applications.libro.models import LibroModel

# CMannagers

from .managers import PrestamosManager

class LectorModel(models.Model):
    """Model definition for Lector."""

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
        max_length=20
    )
    edad = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectors'

    def __str__(self):
        """Unicode representation of Lector."""
        return self.nombre + ' ' + self.apellido
    
class PrestamoModel(models.Model):
    """Model definition for Prestamo."""

    # TODO: Define fields here
    
    lector = models.ForeignKey(
        LectorModel, 
        on_delete=models.CASCADE,
        related_name= 'prestamo'
    )
    libro = models.ForeignKey(
        LibroModel, 
        on_delete=models.CASCADE,
        related_name= 'libro_prestamo'
    )
    fecha_prstamo = models.DateField(
        'Retiro el Libro', 
        auto_now=False, 
        auto_now_add=False
    )
    fecha_devolucion = models.DateField(
        'Devolvio el Libro', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True,
    )
    devuelto = models.BooleanField()
    objects = PrestamosManager()

    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        """Unicode representation of Prestamo."""
        return self.libro.titulo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          


