import datetime

from django.db import models

from django.db.models import Q, Count


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
    
    # Filtra libros de una determinada categoria
    def  listar_libros_categoria(self, categoria):
        
        return self.filter(
            categoria__nombre__icontains = categoria.capitalize()
        ).order_by('titulo')
    
    # Nos permite agregar un autor a un registro de un libro
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id = libro_id)
        libro.autores.add(autor)
        return libro
    
      # Nos permite eliminar un autor a un registro de un libro
    def eliminar_autor_libro(self, libro_id, autor):
        libro = self.get(id = libro_id)
        libro.autores.delete(autor)
        return libro
    
    def libros_num_prestamos (self):
        resultado = self.aggregate(
            num_prestamos = Count('prestamo')
        )
        return resultado
    
    
class CategoriaManager (models.Manager):
   
    # Filtra las categorias correspondiientes al autor.  Distinct nos permite que no repita los nombres de los autores en el caso que tenga mas de un libro en la misma categoria.
    def categoria_por_autor (self, autor):
        
        return self.filter(
            categoria_libro__autores__id = autor
        ).distinct()
    
    # Lista todas las categorias y indica la cantidad de libros que hay en cada una de ellos 
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros  = Count('categoria_libro')
        )
        return resultado
    