from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class PosicionFutbol(str, Enum):
    PORTERO = "PORTERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"
    EXTREMO = "EXTREMO"


db_jugadores = [
    {
        "id": 1,
        "name": "Lionel Messi",
        "dorsal": 10,
        "altura": 1.70,
        "posicion": PosicionFutbol.DELANTERO,
        "equipo": "Inter Miami"
    },
    {
        "id": 2,
        "name": "Dibu Martinez",
        "dorsal": 23,
        "altura": 1.95,
        "posicion": PosicionFutbol.PORTERO,
        "equipo": "Aston Villa"
    }
]



@app.get("/")
def inicio():
    return {"mensaje": "API de Jugadores de Fútbol"}

@app.get("/jugadores")
def mostrar_todos():
    """Muestra la totalidad de los jugadores"""
    return db_jugadores

@app.get("/jugadores/{player_id}")
def show_one_player(player_id: int):
    """Busca un jugador por su ID"""
    for jugador in db_jugadores:
        if jugador["id"] == player_id:
            return jugador
    return {"error": "Jugador no encontrado"}

@app.get("/comparar/{id1}/{id2}")
def compare_two_players(id1: int, id2: int):
    """Compara dos jugadores"""
    p1 = next((j for j in db_jugadores if j["id"] == id1), None)
    p2 = next((j for j in db_jugadores if j["id"] == id2), None)
    return {"jugador1": p1, "jugador2": p2}

@app.get("/equipo/{nombre_equipo}")
def show_equipo(nombre_equipo: str):
    """Muestra los jugadores de un equipo específico"""
    resultado = [j for j in db_jugadores if j["equipo"].lower() == nombre_equipo.lower()]
    return resultado
