from django.contrib import admin

from applications.libro.models import CategoriaModel, LibroModel

# Register your models here.

admin.site.register(CategoriaModel)
admin.site.register(LibroModel)