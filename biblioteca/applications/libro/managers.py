import datetime

from django.db import models

from django.db.models import Q


class LibroManager (models.Manager):
    # Listar los libros
    def listar_libros(self,):
        return self.all()
    
    # Filtra libros por el titulo
    def buscar_libros2(self, kword):
        resultado = self.filter(
            titulo__icontains = kword.capitalize()
        )
        return resultado

    # Filtra libros por el titulo y un rango de fechas
    def buscar_libros3(self, kword):
        resultado = self.filter(
            titulo__icontains = kword.capitalize(),
            fecha__range = ('1980-01-01','2000-01-01')
        )
        return resultado
    
    # Filtra libros por el titulo o por la fecha indicada
    def buscar_libros4(self, kword, fecha1, fecha2):
        
        # De esta maneraconfiguramos la forma en la que se debe ingresar la fecha 4 dijitos
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        
        resultado = self.filter(
            titulo__icontains = kword.capitalize(),
            fecha__range = (date1 ,date2)
        )
        return resultado