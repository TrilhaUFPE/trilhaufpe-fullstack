# Trilha UFPE · Full Stack

Repositório das atividades do bloco Full Stack do Trilha UFPE.

| Atividade | Aula | O que você faz | Onde |
|---|---|---|---|
| **Atividade 1 · API em memória** | Aula 7 · Back-end e APIs | Completar uma API de eventos com FastAPI | `app/main.py` |
| **Atividade 2 · SQL** | Aula 8 · Banco de dados | Criar as tabelas e escrever 5 consultas | `atividade-2/` |

Os prazos estão na página de cada aula, no site do Trilha UFPE. Os testes automáticos dizem o que já está certo e o que falta.

## 1. Preparar o ambiente (uma vez só)

Você precisa de **Python 3.9 ou mais novo**, **Git** e uma conta no **GitHub**.

1. No GitHub, clique em **Fork** neste repositório para criar a sua cópia. No seu fork, abra a aba **Actions** e clique para habilitar os workflows.
2. Clone a **sua** cópia e instale as dependências:

```bash
git clone https://github.com/SEU_USUARIO/trilhaufpe-fullstack.git
cd trilhaufpe-fullstack
python3 -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Rode os testes:

```bash
pytest
```

No começo quase todos falham. É esperado: os testes descrevem o que você ainda vai fazer.

## 2. Atividade 1 · API em memória

A API guarda eventos num dicionário Python. A rota que lista os eventos (`GET /events`) já funciona e serve de modelo. Complete os 4 `TODO` de `app/main.py`:

| TODO | Endpoint | Resposta esperada |
|---|---|---|
| 1 | `GET /events/{event_id}` | **200** com o evento · **404** `"Evento não encontrado"` |
| 2 | `POST /events` | **201** com o evento criado e um `id` novo |
| 3 | `POST /events` com dados inválidos | **422** para título vazio ou capacidade menor ou igual a zero, sem guardar nada |
| 4 | `DELETE /events/{event_id}` | **204** sem corpo · **404** `"Evento não encontrado"` |

Para testar no navegador, suba o servidor e abra http://127.0.0.1:8000/docs:

```bash
uvicorn app.main:app --reload
```

Para rodar só os testes desta atividade: `pytest tests/test_api.py`

## 3. Atividade 2 · SQL

O enunciado completo está em [`atividade-2/README.md`](atividade-2/README.md). Você escreve dois arquivos:

- `atividade-2/schema.sql`: o `CREATE TABLE` das tabelas `events`, `users` e `registrations`.
- `atividade-2/consultas.sql`: 5 consultas `SELECT`.

Para rodar só os testes desta atividade: `pytest tests/test_sql.py`

## 4. Entregar

```bash
git add -A
git commit -m "Conclui atividade 1"
git push
```

Confira a aba **Actions** do seu fork. Cada atividade tem o seu check: **Atividade 1 · API** e **Atividade 2 · SQL**. O check da atividade que você está entregando precisa ficar verde; o da outra pode continuar vermelho enquanto você não chega nela. Depois, envie o link do seu fork pelo formulário da página da aula.

## Dúvidas

Pergunte no grupo da turma. Mande o comando que você rodou, a mensagem de erro completa e o que você esperava que acontecesse.

Pode usar IA para entender um erro ou um conceito, mas escreva a solução você mesmo: o objetivo é aprender o caminho, não só chegar na resposta.
