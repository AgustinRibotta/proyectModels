from django.db import models

from django.db.models import Q


class AutorManager (models.Manager):
    # Manager para Modelo Autor
    # Listar los autores
    def listar_autores(self,):
        return self.all()
    
    # Filtra los autores por el nombre
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains = kword.capitalize()
        )
        return resultado

    # Filtra los autores por el nombre o por el apellido
    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains = kword.capitalize()) | Q(apellido__icontains = kword.capitalize())
        )
        return resultado

    # Filtra los autores por el nombre pero excluye a los que tengan 0 o 56
    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombre__icontains = kword
        ).exclude(
            Q(adad__icontains = 0) | Q(adad__icontains = 56)
        )
        return resultado

    # Filtra a los autores que sean mayor de 40, menor de 65 y los ordena por apellido y nombre.
    def buscar_autor4(self, kword):
        resultado = self.filter(
            adad__gt = 40,
            adad__lt = 65
        ).order_by('apellido','nombre', 'id')
        return resultado

