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

