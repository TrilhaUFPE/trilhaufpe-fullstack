"""API de eventos do Trilha UFPE · Atividade 1.

Rode o servidor com:
    uvicorn app.main:app --reload

E abra a documentação interativa em http://127.0.0.1:8000/docs
"""
from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Eventos do Trilha")


class EventInput(BaseModel):
    """O contrato: o que o cliente precisa mandar para criar um evento."""

    title: str
    date: date
    capacity: int


# "Banco" em memória: um dicionário que liga o id ao evento.
# Ele some toda vez que o servidor reinicia (na Aula 8 isso vira um banco de verdade).
events = {
    1: {"id": 1, "title": "Oficina de Python", "date": date(2026, 10, 10), "capacity": 2},
}


@app.get("/events")
def list_events():
    """Lista todos os eventos. Já está pronto: use como modelo."""
    return list(events.values())


@app.get("/events/{event_id}")
def get_event(event_id: int):
    # TODO 1: devolva o evento com esse id.
    #         Se ele não existir, responda 404 com detail="Evento não encontrado".
    raise HTTPException(status_code=501, detail="Ainda não implementado")


@app.post("/events", status_code=201)
def create_event(event: EventInput):
    # TODO 2: crie o evento com um id novo, guarde em `events` e devolva o evento criado.
    # TODO 3: recuse com 422 um título vazio e uma capacidade menor ou igual a zero.
    #         Dica: isso se resolve no EventInput, com o Field do Pydantic.
    raise HTTPException(status_code=501, detail="Ainda não implementado")


@app.delete("/events/{event_id}", status_code=204)
def delete_event(event_id: int):
    # TODO 4: apague o evento. A resposta 204 não tem corpo.
    #         Se ele não existir, responda 404 com detail="Evento não encontrado".
    raise HTTPException(status_code=501, detail="Ainda não implementado")
