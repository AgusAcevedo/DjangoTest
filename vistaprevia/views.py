from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from productos.models import Producto
# Create your views here.
"""
def index(request):
    return HttpResponse("Hola mundo!")
"""

def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    producto = Producto.objects.filter( Q(estado="Publicado"),)
    params['producto']=producto
    print(producto)
    return render(request,'vistaprevia/index.html', params)