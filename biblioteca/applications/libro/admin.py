from django.contrib import admin

from applications.libro.models import CategoriaModel, LibroModel

# Register your models here.

admin.site.register(CategoriaModel)



@admin.register(LibroModel)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('categoria',)
    list_filter = ('categoria',)
    
    
# admin.site.register(LibroModel, Admin)