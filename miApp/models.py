from django.db import models

class Libros(models.Model):
    nombre_producto = models.CharField(max_length=100)
    Autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100,default="No definido")
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    Descripcion = models.CharField(max_length=1000)
    Imagen = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.nombre_producto