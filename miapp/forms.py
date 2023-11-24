from django import forms
from .models import Prueba
from django_ckeditor_5.widgets import CKEditor5Widget
from ckeditor.widgets import CKEditorWidget

class FormularioTesting(forms.Form):
    titulo = forms.CharField(label='Titulo')
    descripcion = forms.CharField(label="Descripcion", widget=CKEditorWidget())

class FormularioModelo(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = '__all__'
        widgets = {
            "descripcion": CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'},
            )
        }