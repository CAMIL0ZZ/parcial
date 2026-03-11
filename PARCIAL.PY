from fastapi import FastAPI
from pydantic import BaseModel


class jugador(BaseModel):
    id: int
    name: str
    date: str
    altura: float
    posicionfutbol: str
    equipo: str