from django.urls import path
from .views import *

urlpatterns = [
    path('',listar_productos, name='listado_productos'),
    path('crear/', crear_producto, name="crear_producto"),
    path('editar/<id>', editar_producto, name="editar_producto"),
    path('actualizar/<id>', actualizar_producto, name="actualizar_producto"),
    
]
