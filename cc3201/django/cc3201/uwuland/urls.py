from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        
    path("players/", views.players, name="players"),
    path("player_id/", views.player_id, name="player_id"),
    path("partidos/", views.partidos_por_equipo, name="partidos_por_equipo"),
    path("jugadores/", views.jugadores_por_equipo, name="jugadores_por_equipo"),
    path("ficha_jugador", views.estadisticas_jugador, name="estadisticas_jugador")
]
