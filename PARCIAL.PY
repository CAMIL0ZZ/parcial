from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class PosicionFutbol(str, Enum):
    PORTERO = "PORTERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"
    EXTREMO = "EXTREMO"

class Jugador(BaseModel):
    id: int
    name: str
    dorsal: int
    date_nacimiento: str
    altura: float
    posicion: PosicionFutbol
    equipo: str

db_jugadores = [
    Jugador(id=1, name="Lionel Messi", dorsal=10, date_nacimiento="1987-06-24", altura=1.70, posicion=PosicionFutbol.DELANTERO, equipo="Inter Miami"),
    Jugador(id=2, name="Dibu Martinez", dorsal=23, date_nacimiento="1992-09-02", altura=1.95, posicion=PosicionFutbol.PORTERO, equipo="Aston Villa")
]


@app.get("/")
def inicio():
    return {"mensaje": "API de Fútbol funcionando"}

@app.get("/jugadores")
def get_all_players():
    """Muestra todos los jugadores"""
    return db_jugadores

@app.get("/jugadores/{player_id}")
def show_one_player(player_id: int):
    """Muestra un solo jugador"""
    for j in db_jugadores:
        if j.id == player_id:
            return j
    return {"error": "Jugador no encontrado"}

@app.get("/jugadores/equipo/{nombre_equipo}")
def get_players_by_team(nombre_equipo: str):
    """Muestra jugadores por equipo"""
    return [j for j in db_jugadores if j.equipo.lower() == nombre_equipo.lower()]