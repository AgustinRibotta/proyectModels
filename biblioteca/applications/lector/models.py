from collections.abc import Iterable
from django.db import models


# CMannagers
from .managers import PrestamosManager
# Models
from applications.autor.models import Personas
from applications.libro.models import LibroModel


class LectorModel(Personas):


    class Meta:

        verbose_name = 'Lector '
        verbose_name_plural = 'Lectores'

    
class PrestamoModel(models.Model):

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
    fecha_prstamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True,
        null=True,
    )
    devuelto = models.BooleanField()
    objects = PrestamosManager()

    # Sobrescribimos la funcion save, para modificar camposm directamente desde el administrador de Django
    
    def save(self, *arg, **kwargs):
        
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        
        super(PrestamoModel, self).save(*arg, **kwargs)
    
    
    class Meta:

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):

        return self.libro.titulo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          


