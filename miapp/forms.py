from django import forms
from ckeditor.widgets import CKEditorWidget

class FormularioTesting(forms.Form):
    titulo = forms.CharField(label='Titulo')
    descripcion = forms.CharField(widget=CKEditorWidget)