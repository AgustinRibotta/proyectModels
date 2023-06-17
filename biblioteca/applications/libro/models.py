from django.db import models

from applications.autor.models import AutorModel

# Create your models here.


class CategoriaModel(models.Model):
    """Model definition for Categoria."""

    # TODO: Define fields here
    nombre = models.CharField(
        'Nombre', 
        max_length=30
    )
    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre
    

class LibroModel(models.Model):
    """Model definition for Libro."""

    # TODO: Define fields here
    categoria = models.ForeignKey(
        CategoriaModel, 
        on_delete=models.CASCADE
    )
    autores = models.ManyToManyField(AutorModel)
    titulo = models.CharField(
        'Titulo', 
        max_length=50
    )
    fecha = models.DateField(
        'Fehca de Lanzamiento', 
        auto_now=False, 
        auto_now_add=False
    )
    portada = models.ImageField(
        'Foto de Portada', 
        upload_to='portada', 
        height_field=None, width_field=None,
        max_length=None
    )
    visitas = models.PositiveIntegerField()
    
    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        """Unicode representation of Libro."""
        return self.titulo + ' ' + self.categoria
