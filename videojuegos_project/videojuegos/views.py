from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuego
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Vista de registro
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada con éxito! Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

# Vista de login
def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('listar_videojuegos')  # Cambia 'home' a tu vista principal
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Vista de logout
def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada con éxito.")
    return redirect('login')

# Leer (Listar Videojuegos)
def listar_videojuegos(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para acceder a esta página.")
        return redirect('login')
    
    videojuegos = Videojuego.objects.all()
    return render(request, 'listar_videojuegos.html', {'videojuegos': videojuegos})

# Crear
def crear_videojuego(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para acceder a esta página.")
        return redirect('login')
    
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

