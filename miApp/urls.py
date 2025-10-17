from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('detalles/<int:id>',views.detalle_libro, name="detalles"),
    path('categorias/<str:genero>',views.categoria_libro, name="categorias"),
]