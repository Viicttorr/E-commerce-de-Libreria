from django.contrib import admin
from .models import Libros


@admin.register(Libros)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'Autor', 'genero', 'precio','stock','Descripcion','Imagen')