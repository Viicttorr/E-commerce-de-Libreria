from django.shortcuts import render
from .models import Libros

# Create your views here.

def main(request):
    context = {}
    libros = Libros.objects.all()
    context['libros']= libros
    return render(request,"index.html",context)

def detalle_libro(request, id):
    context = {}
    libro = Libros.objects.get(id=id)
    context['libro']= libro
    return render(request,"detalle.html",context)

def categoria_libro(request,genero):
    context = {}
    categorias = Libros.objects.filter(genero=genero)
    context['categorias']= categorias
    return render(request,"categoria.html",context)