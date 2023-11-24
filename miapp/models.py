from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = CKEditor5Field('Descripcion', config_name='default')