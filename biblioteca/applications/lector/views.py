# Python
from datetime import date
# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
# Models
from .models import PrestamoModel
# Forms
from .forms import MultiplePrestamoForm, PrestamoForm

class RegistrarPersonaFormView (FormView):
    template_name = 'lector/add.html'
    form_class = PrestamoForm
    success_url = '.'
    
    
    # De esta forma creamos una validacion que nos permite verificar el libro que se esta solicitando si tiene estock y en el caso que lo tenga restarle uno.
    def form_valid(self, form):
        
        # De esta manera crea uno neuvo
        # PrestamoModel.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prstamo = date.today(),
        #     devuelto = False,
        # )
        
        # De esta manera crea uno actualiza
        prestamo = PrestamoModel(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prstamo = date.today(),
            devuelto = False,
        )
        prestamo.save()
        
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock -1
        libro.save()
        
        return super(RegistrarPersonaFormView, self).form_valid(form)


class AddPersonaFormView (FormView):
    template_name = 'lector/add.html'
    form_class = PrestamoForm
    success_url = '.'
    
    
    # Valida si el libro que ya fue solicitado por la persona, en el caso que no, crea un registro, de lo con traio tira erro.
    def form_valid(self, form):
        
        obj, created = PrestamoModel.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults={
                'fecha_prstamo' : date.today(),
            }
        )
        
        if created:
            return super(AddPersonaFormView, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
    

class AddMultiplePersonaFormView (FormView):
    template_name = 'lector/addmultiple.html' 
    form_class = MultiplePrestamoForm
    success_url = '.'
    
    

    def form_valid(self, form):     
        prestamos = []
        
        
        for l in form.cleaned_data['libros']:
            prestamo = PrestamoModel(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prstamo = date.today(),
                devuelto = False,
            )
            
            prestamos.append(prestamo)
            
        PrestamoModel.objects.bulk_create(
            prestamos
        )

        return super(AddMultiplePersonaFormView, self).form_valid(form)