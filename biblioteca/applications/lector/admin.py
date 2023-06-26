from django.contrib import admin

from applications.lector.models import LectorModel, PrestamoModel

# Register your models here.
admin.site.register(LectorModel)

@admin.register(PrestamoModel)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = (
        'libro',
        'lector',
        'fecha_prstamo',
        'fecha_devolucion',
        'devuelto',
    )
    list_filter = (
        'lector',
        'libro',
    )
    search_fields = [
        "libro__titulo",
        "lector__nombres",
    ]

    
