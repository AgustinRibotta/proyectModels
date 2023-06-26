from django import forms
# Models App Libros
from applications.libro.models import LibroModel

# Models 
from .models import PrestamoModel

class PrestamoForm(forms.ModelForm):
    """Form definition for Prestamo."""

    class Meta:
        """Meta definition for Prestamoform."""

        model = PrestamoModel
        fields = (
            'lector',
            'libro',
        )
        
        
class MultiplePrestamoForm(forms.ModelForm):

    # Conjunto de item relacionados a un modelo.
    libros = forms.ModelMultipleChoiceField(
        queryset= None,
        required= True,
        widget= forms.CheckboxSelectMultiple,
    )

    class Meta:
        """Meta definition for Prestamoform."""

        model = PrestamoModel
        fields = (
            'lector',
        )

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = LibroModel.objects.all()
    