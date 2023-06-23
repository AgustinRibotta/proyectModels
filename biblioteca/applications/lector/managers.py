import datetime

from django.db import models

from django.db.models import Q, Count, Avg , Sum
from django.db.models.functions import Lower    

# El aggregate devuelve un dicicoonario por ende se puede aplicar todas las funciones correspondientes al mistmo

class PrestamosManager (models.Manager):
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id ='17'
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector__edad'),
        )
        return resultado
    
    def num_libros_prestados(self):
        resulado = self.values(
            'libro'    
        ).annotate(
            num_prstamos = Count('libro'),
            titulo = Lower('libro__titulo',),
        )
        for r in resulado:
            print (r, r['num_prstamos'])
            
        return resulado