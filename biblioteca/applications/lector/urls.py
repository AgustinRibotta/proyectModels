
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'perstamo/registrar/',
        views.RegistrarPersonaFormView.as_view(),
        name='Prestamo-registrar'
    ),
    path(
        'perstamo/add/',
        views.AddPersonaFormView.as_view(),
        name='Prestamo-add'
    ),
    path(
        'prestamo/multiple/',
        views.AddMultiplePersonaFormView.as_view(),
        name='Multiple'
    ),
]
