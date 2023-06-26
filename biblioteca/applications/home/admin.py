from django.contrib import admin

# Register your models here.

from .models import PersonaModel, EmpleadoModel

admin.site.register(PersonaModel)
admin.site.register(EmpleadoModel)