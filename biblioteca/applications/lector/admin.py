from django.contrib import admin

from applications.lector.models import LectorModel, PrestamoModel

# Register your models here.
admin.site.register(LectorModel)
admin.site.register(PrestamoModel)