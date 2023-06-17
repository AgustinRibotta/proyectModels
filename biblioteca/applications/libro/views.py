from django.shortcuts import render
from django.views.generic import ListView

# Modelos
from .models import LibroModel

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
        
    

