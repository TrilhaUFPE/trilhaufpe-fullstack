"""Testes da Atividade 1. Eles são o enunciado: leia antes de programar.

Rode só estes com:  pytest tests/test_api.py
"""
import copy

import pytest
from fastapi.testclient import TestClient

from app import main

EVENTO_INICIAL = copy.deepcopy(main.events)
NOVO_EVENTO = {"title": "Semana de Tecnologia", "date": "2026-10-20", "capacity": 40}


@pytest.fixture
def api():
    """Cada teste começa com só o evento inicial guardado."""
    main.events.clear()
    main.events.update(copy.deepcopy(EVENTO_INICIAL))
    return TestClient(main.app)


# ---------- pronto desde o início ----------

def test_lista_os_eventos(api):
    resposta = api.get("/events")
    assert resposta.status_code == 200
    assert [e["title"] for e in resposta.json()] == ["Oficina de Python"]


# ---------- TODO 1: buscar por id ----------

def test_busca_um_evento_pelo_id(api):
    resposta = api.get("/events/1")
    assert resposta.status_code == 200
    assert resposta.json() == {
        "id": 1,
        "title": "Oficina de Python",
        "date": "2026-10-10",
        "capacity": 2,
    }


def test_evento_que_nao_existe_da_404(api):
    resposta = api.get("/events/999")
    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Evento não encontrado"


# ---------- TODO 2: criar ----------

def test_cria_um_evento(api):
    resposta = api.post("/events", json=NOVO_EVENTO)
    assert resposta.status_code == 201

    criado = resposta.json()
    assert criado["title"] == NOVO_EVENTO["title"]
    assert criado["date"] == NOVO_EVENTO["date"]
    assert criado["capacity"] == NOVO_EVENTO["capacity"]
    assert isinstance(criado["id"], int) and criado["id"] > 0

    # depois de criado, o evento aparece na lista e na busca por id
    assert len(api.get("/events").json()) == 2
    assert api.get(f"/events/{criado['id']}").json()["title"] == NOVO_EVENTO["title"]


def test_cada_evento_criado_ganha_um_id_novo(api):
    primeiro = api.post("/events", json=NOVO_EVENTO).json()["id"]
    segundo = api.post("/events", json={**NOVO_EVENTO, "title": "Hackathon Trilha"}).json()["id"]
    assert len({1, primeiro, segundo}) == 3


# ---------- TODO 3: validar a entrada ----------

@pytest.mark.parametrize(
    "corpo",
    [
        {**NOVO_EVENTO, "title": ""},
        {**NOVO_EVENTO, "capacity": 0},
        {**NOVO_EVENTO, "capacity": -5},
        {**NOVO_EVENTO, "date": "amanhã"},
        {"date": "2026-10-20", "capacity": 40},
    ],
    ids=["titulo-vazio", "capacidade-zero", "capacidade-negativa", "data-invalida", "sem-titulo"],
)
def test_entrada_invalida_da_422_e_nao_guarda_nada(api, corpo):
    resposta = api.post("/events", json=corpo)
    assert resposta.status_code == 422
    assert len(api.get("/events").json()) == 1


# ---------- TODO 4: apagar ----------

def test_apaga_um_evento(api):
    resposta = api.delete("/events/1")
    assert resposta.status_code == 204
    assert resposta.content == b""
    assert api.get("/events/1").status_code == 404
    assert api.get("/events").json() == []


def test_apagar_evento_que_nao_existe_da_404(api):
    resposta = api.delete("/events/999")
    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Evento não encontrado"
