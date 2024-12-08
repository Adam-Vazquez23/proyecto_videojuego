from django.urls import path
from . import views



urlpatterns = [
    path('crear/', views.crear_videojuego, name='crear_videojuego'),
    path('actualizar/<int:id>/', views.actualizar_videojuego, name='actualizar_videojuego'),
    path('borrar/<int:id>/', views.borrar_videojuego, name='borrar_videojuego'),
    path('listar', views.listar_videojuegos, name='listar_videojuegos'),
    path('registro/', views.registro, name='registro'),
    path('', views.inicio_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

]
