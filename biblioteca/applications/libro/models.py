from django.db import models
from django.db.models.signals import post_save
#App de terceros
from PIL import Image
# Models
from applications.autor.models import AutorModel
# Managers
from applications.libro.managers import LibroManager, CategoriaManager



class CategoriaModel(models.Model):
    """Model definition for Categoria."""

    # TODO: Define fields here
    nombre = models.CharField(
        'Nombre', 
        max_length=30
    )
    objects = CategoriaManager()
    
    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return  self.nombre 
    

class LibroModel(models.Model):
    """Model definition for Libro."""

    # TODO: Define fields here
    categoria = models.ForeignKey(
        CategoriaModel, 
        on_delete=models.CASCADE,
        # Con esto relacionamos la categoria con los libros
        related_name= 'categoria_libro'
    )
    autores = models.ManyToManyField(AutorModel)
    titulo = models.CharField(
        'Titulo', 
        max_length=50,
    )
    fecha = models.DateField(
        'Fehca de Lanzamiento', 
        auto_now=False, 
        auto_now_add=False,
    )
    portada = models.ImageField(
        'Foto de Portada', 
        upload_to='portada', 
        height_field=None, 
        width_field=None,
        max_length=None,
        blank=True,
        null=True
    )
    visitas = models.PositiveIntegerField(
        blank=True,
        null=True
    )       
    stock = models.PositiveIntegerField(
        default=0
    )       
    objects = LibroManager()
    
    
    # Todo aquello que no es un atributo en el modelo o base de datos
    class Meta:
        """Meta definition for Libro."""
       

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo','fecha']

    def __str__(self):
        """Unicode representation of Libro."""
        return str(self.id) + ' - ' + self.titulo 


def optimize_imagen(sender, instance, **kwargs):
    
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality= 20, optimize=True)

post_save.connect(optimize_imagen, sender= LibroModel)
