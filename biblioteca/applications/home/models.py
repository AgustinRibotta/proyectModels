from django.db import models

# Create your models here.

class PersonaModel(models.Model):
    """Model definition for Persona."""

    ful_name = models.CharField('Nombre completo', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)
    
    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        # Nombre en base de datos
        db_table = 'personas'
        # No se puedan repetir dos valores
        unique_together = ['pais', 'apelativo',]
        # No se puede regestrar datos segun la edad
        constraints = [
            models.CheckConstraint(check = models.Q(edad__gte = 18), name= 'Debes ser mayor de edad.')
        ]
        # Lo creamos como modelo pero no lo generamos en la base de datos (herencia)
        abstract = True
        
    def __str__(self):
        """Unicode representation of Persona."""
        return self.ful_name


class EmpleadoModel(PersonaModel):
    """Model definition for Empleado."""

    empleado = models.CharField('Empleo', max_length=50)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        pass


class ClienteModel(PersonaModel):
    """Model definition for Empleado."""

    email = models.EmailField('Correo', max_length=254)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        pass
