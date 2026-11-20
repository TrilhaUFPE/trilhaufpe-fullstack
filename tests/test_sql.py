"""Testes da Atividade 2. Eles rodam o seu schema.sql e o seu consultas.sql num SQLite em memória.

Rode só estes com:  pytest tests/test_sql.py
"""
import re
import sqlite3
from pathlib import Path

import pytest

PASTA = Path(__file__).resolve().parent.parent / "atividade-2"


@pytest.fixture
def banco():
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript((PASTA / "schema.sql").read_text(encoding="utf-8"))
    try:
        con.executescript((PASTA / "dados.sql").read_text(encoding="utf-8"))
    except sqlite3.Error as erro:
        pytest.fail(f"O dados.sql não entrou no seu schema: {erro}")
    yield con
    con.close()


def consulta(numero):
    texto = (PASTA / "consultas.sql").read_text(encoding="utf-8")
    partes = re.split(r"^--\s*Q(\d)\b.*$", texto, flags=re.M)
    respostas = {int(n): sql for n, sql in zip(partes[1::2], partes[2::2])}
    sql = respostas.get(numero, "")
    sem_comentarios = re.sub(r"--.*$", "", sql, flags=re.M).strip()
    if not sem_comentarios:
        pytest.fail(f"A consulta Q{numero} ainda não foi escrita no consultas.sql")
    return sql


# ---------- Parte 1: as tabelas ----------

def test_as_tres_tabelas_existem(banco):
    nomes = {linha[0] for linha in banco.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    assert {"events", "users", "registrations"} <= nomes


def test_os_dados_de_exemplo_entram(banco):
    contar = lambda tabela: banco.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()[0]
    assert (contar("events"), contar("users"), contar("registrations")) == (4, 4, 6)


@pytest.mark.parametrize(
    "comando",
    [
        "INSERT INTO registrations (event_id, user_id) VALUES (999, 1)",
        "INSERT INTO registrations (event_id, user_id) VALUES (1, 999)",
    ],
    ids=["evento-inexistente", "usuario-inexistente"],
)
def test_inscricao_precisa_apontar_para_algo_que_existe(banco, comando):
    with pytest.raises(sqlite3.IntegrityError):
        banco.execute(comando)


def test_a_mesma_pessoa_nao_se_inscreve_duas_vezes_no_mesmo_evento(banco):
    with pytest.raises(sqlite3.IntegrityError):
        banco.execute("INSERT INTO registrations (event_id, user_id) VALUES (1, 1)")


def test_capacidade_precisa_ser_positiva(banco):
    with pytest.raises(sqlite3.IntegrityError):
        banco.execute("INSERT INTO events (title, date, capacity) VALUES ('Inválido', '2026-12-01', 0)")


def test_evento_precisa_de_titulo(banco):
    with pytest.raises(sqlite3.IntegrityError):
        banco.execute("INSERT INTO events (date, capacity) VALUES ('2026-12-01', 10)")


# ---------- Parte 2: as consultas ----------

ESPERADO = {
    1: [
        ("Palestra de Carreira", "2026-09-28"),
        ("Oficina de Python", "2026-10-10"),
        ("Semana de Tecnologia", "2026-10-20"),
        ("Hackathon Trilha", "2026-11-07"),
    ],
    2: [("Hackathon Trilha",), ("Palestra de Carreira",), ("Semana de Tecnologia",)],
    3: [("Ana",), ("Bruno",)],
    4: [("Hackathon Trilha",), ("Semana de Tecnologia",)],
    5: [
        ("Oficina de Python", 2),
        ("Semana de Tecnologia", 2),
        ("Hackathon Trilha", 1),
        ("Palestra de Carreira", 1),
    ],
}


@pytest.mark.parametrize("numero", sorted(ESPERADO), ids=[f"Q{n}" for n in sorted(ESPERADO)])
def test_consulta(banco, numero):
    linhas = [tuple(linha) for linha in banco.execute(consulta(numero)).fetchall()]
    assert linhas == ESPERADO[numero]
