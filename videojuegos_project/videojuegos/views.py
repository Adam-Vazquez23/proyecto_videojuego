from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuego
from django.http import HttpResponse
from django.template import loader

# Leer (Listar Videojuegos)
def listar_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'listar_videojuegos.html', {'videojuegos': videojuegos})

# Crear
def crear_videojuego(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        genero = request.POST['genero']
        fecha_lanzamiento = request.POST['fecha_lanzamiento']
        desarrollador = request.POST['desarrollador']
        precio = request.POST['precio']
        Videojuego.objects.create(
            titulo=titulo, genero=genero, 
            fecha_lanzamiento=fecha_lanzamiento, 
            desarrollador=desarrollador, precio=precio)
        return redirect('listar_videojuegos')
    return render(request, 'crear_videojuego.html')

# Actualizar
def actualizar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        videojuego.titulo = request.POST['titulo']
        videojuego.genero = request.POST['genero']
        videojuego.fecha_lanzamiento = request.POST['fecha_lanzamiento']
        videojuego.desarrollador = request.POST['desarrollador']
        videojuego.precio = request.POST['precio']
        videojuego.save()
        return redirect('listar_videojuegos')
    return render(request, 'actualizar_videojuego.html', {'videojuego': videojuego})

# Borrar
def borrar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, id=id)
    videojuego.delete()
    return redirect('listar_videojuegos')

def index(request):
    return HttpResponse("Bienvenido a la sección de videojuegos.")