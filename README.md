# Trilha UFPE · Full Stack

Repositório das atividades do bloco Full Stack do Trilha UFPE.

| Atividade | Aula | O que você faz | Onde |
|---|---|---|---|
| **Atividade 1 · API em memória** | Aula 7 · Back-end e APIs | Completar uma API de eventos com FastAPI | `app/main.py` |
| **Atividade 2 · SQL** | Aula 8 · Banco de dados | Criar as tabelas e escrever 5 consultas | `atividade-2/` |

Os prazos estão na página de cada aula, no site do Trilha UFPE. Os testes automáticos dizem o que já está certo e o que falta.

## 1. Preparar o ambiente (uma vez só)

A configuração é feita em casa, antes de começar a Atividade 1. Leva uns 20 minutos na primeira vez.

### 1.1 Instale as ferramentas

Você precisa de **Python 3.9 ou mais novo**, **Git** e uma conta no **GitHub** (github.com, gratuita).

| Sistema | Python | Git |
|---|---|---|
| **Windows** | Baixe em python.org/downloads. No instalador, marque **"Add python.exe to PATH"** antes de clicar em Install. | Baixe em git-scm.com e aceite as opções padrão. |
| **macOS** | Baixe em python.org/downloads (ou `brew install python`). | Rode `git --version` no Terminal: se não tiver, o macOS oferece instalar. |
| **Linux (Ubuntu)** | `sudo apt install python3 python3-venv python3-pip` | `sudo apt install git` |

Confira num terminal novo (no Windows, use o **PowerShell**):

```bash
python3 --version     # no Windows: python --version
git --version
```

### 1.2 Faça o fork e habilite os testes no GitHub

1. Entre na sua conta do GitHub e abra este repositório.
2. Clique em **Fork** (canto superior direito) e depois em **Create fork**. Agora existe uma cópia em `github.com/SEU_USUARIO/trilhaufpe-fullstack`.
3. No **seu fork**, abra a aba **Actions** e clique em **"I understand my workflows, go ahead and enable them"**. Sem isso, os testes não rodam no GitHub.

### 1.3 Clone o seu fork e crie o ambiente

Troque `SEU_USUARIO` pelo seu usuário do GitHub. Clone o **seu fork**, não este repositório.

**macOS e Linux:**

```bash
git clone https://github.com/SEU_USUARIO/trilhaufpe-fullstack.git
cd trilhaufpe-fullstack
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
git clone https://github.com/SEU_USUARIO/trilhaufpe-fullstack.git
cd trilhaufpe-fullstack
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Com a `.venv` ativada, o terminal mostra `(.venv)` no começo da linha. **Toda vez que abrir um terminal novo, ative de novo** (o comando `source` ou `Activate.ps1` acima, dentro da pasta do projeto).

### 1.4 Rode os testes

```bash
pytest
```

No começo quase todos falham. É esperado: os testes descrevem o que você ainda vai fazer. O que importa agora é o comando rodar.

### Problemas comuns

| O que aparece | O que fazer |
|---|---|
| `python3: command not found` no Windows | No Windows o comando é `python`. Se nem `python` funcionar, reinstale marcando "Add python.exe to PATH". |
| `pytest: command not found` ou `No module named fastapi` | A `.venv` não está ativada. Ative (passo 1.3) e rode de novo. |
| PowerShell: "execução de scripts foi desabilitada" | Rode uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirme e ative a `.venv` de novo. |
| `git push` pede usuário e senha | O GitHub não aceita a senha da conta. Siga a janela de login que abre no navegador ou use `gh auth login` (GitHub CLI). |
| `Permission denied` no `git push` | Você clonou este repositório em vez do seu fork. Clone de novo a partir de `github.com/SEU_USUARIO/...`. |
| A aba Actions do fork não mostra nada | Os workflows não foram habilitados (passo 1.2, item 3). |
| `Address already in use` ao subir o servidor | Já tem um servidor rodando na porta 8000. Feche o outro terminal ou use `uvicorn app.main:app --reload --port 8001`. |

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
