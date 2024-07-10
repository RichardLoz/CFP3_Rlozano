from django.urls import path
from .views import *

urlpatterns = [
    path('',listar_productos, name='listado_productos'),
]
