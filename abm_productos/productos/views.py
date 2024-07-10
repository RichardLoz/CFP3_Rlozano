from django.shortcuts import render
from .models import Producto

#TODO: LOGICA DE MI APP

def listar_productos(request):
    productos = Producto.objects.all() 
    return render(request, 'producto.html', {'productos': productos})
