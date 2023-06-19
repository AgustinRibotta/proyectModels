
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'libros/',
        views.ListaLibros.as_view(),
        name='Libros'
    ),
    path(
        'libros-2/',
        views.ListLibros2.as_view(),
        name='libros2'
    ),
    path(
        'detalle/<pk>',
        views.LibroDetalle.as_view(),
        name='Detalle'
    ),
    path(
        'lista/',
        views.CategoriaListView.as_view(),
        name='Listado-libros'
    ),
]
