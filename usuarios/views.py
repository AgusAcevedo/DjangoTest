from django.shortcuts import render

# Create your views here.
def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    return render(request,'vistaprevia/index.html', params)