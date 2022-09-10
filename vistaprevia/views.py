from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
def index(request):
    return HttpResponse("Hola mundo!")
"""

def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    return render(request,'vistaprevia/index.html', params)