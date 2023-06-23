from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Modelos
from .models import CategoriaModel, LibroModel

# Create your views here.



class ListaLibros(ListView):
    
    template_name = "libro/lista.html"
    context_object_name = 'lista'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        # Fecha1
        f1 = self.request.GET.get('fecha1', '')
        # Fecah 2
        f2 = self.request.GET.get('fecha2', '')
        
        if f1 and f2:
           return LibroModel.objects.buscar_libros4(palabra_clave, f1, f2)
        else:
           return LibroModel.objects.listar_libros()
       

class ListLibros2(ListView):
    
    template_name = "libro/lista2.html"
    context_object_name = 'lista'
    
    def get_queryset(self):
        
        palabra_clave = self.request.GET.get('kword', '')

        if palabra_clave:
            
            return LibroModel.objects.listar_libros_categoria(palabra_clave)
        
        else:
            return LibroModel.objects.all()
        
        

class LibroDetalle(DetailView):
    model = LibroModel
    template_name = "libro/detalle.html"

    


class CategoriaListView(ListView):

    template_name = "libro/list_categorias.html"
    context_object_name = 'categorias'
    
    def get_queryset(self):

        return CategoriaModel.objects.listar_categoria_libros()
    

class ListaLibrosTrg(ListView):
    
    template_name = "libro/lista.html"
    context_object_name = 'lista'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        return LibroModel.objects.buscar_libros_trg(palabra_clave)
       
