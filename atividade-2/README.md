# Atividade 2 · SQL

A organização do Trilha quer guardar os eventos, as pessoas e quem se inscreveu em quê. Você vai desenhar as tabelas e responder algumas perguntas com consultas SQL.

Não precisa instalar nada: dá para fazer tudo no [sqliteonline.com](https://sqliteonline.com) (escolha o motor **SQLite**). No fim, copie o que você escreveu para os arquivos deste repositório e rode os testes.

## Parte 1 · As tabelas (`schema.sql`)

Crie três tabelas. Os nomes precisam ser exatamente estes, porque o `dados.sql` usa eles:

| Tabela | Colunas | Regras |
|---|---|---|
| `events` | `id`, `title`, `date`, `capacity` | `id` é a chave primária · `title` e `date` são obrigatórios · `capacity` é obrigatória e maior que zero |
| `users` | `id`, `name`, `email` | `id` é a chave primária · `name` e `email` são obrigatórios |
| `registrations` | `id`, `event_id`, `user_id` | `id` é a chave primária · `event_id` aponta para `events` e `user_id` aponta para `users` · a mesma pessoa não pode se inscrever duas vezes no mesmo evento |

Dica: cada regra vira uma restrição da Aula 8 (`PRIMARY KEY`, `NOT NULL`, `CHECK`, `REFERENCES`, `UNIQUE`).

Para conferir no sqliteonline: rode `PRAGMA foreign_keys = ON;`, depois o seu `schema.sql` e depois o `dados.sql`. Os dados precisam entrar sem erro.

## Parte 2 · As consultas (`consultas.sql`)

Escreva uma consulta embaixo de cada marcador do arquivo. Selecione exatamente as colunas pedidas, na ordem pedida.

1. **Q1** · Título e data de todos os eventos, do mais cedo para o mais tarde.
2. **Q2** · Títulos dos eventos com capacidade de pelo menos 30 pessoas, em ordem alfabética.
3. **Q3** · Nomes de quem está inscrito na "Oficina de Python", em ordem alfabética.
4. **Q4** · Títulos dos eventos em que a Carla está inscrita, em ordem alfabética.
5. **Q5** · Para cada evento com inscrições, o título e o número de inscritos, do mais cheio para o mais vazio (empate: ordem alfabética do título).

As Q3 e Q4 precisam de `JOIN`. A Q5 precisa de `COUNT` e `GROUP BY`.

## Conferir

```bash
pytest tests/test_sql.py
```

Quando tudo passar, faça commit e push como na Atividade 1 e envie o link do seu fork pelo formulário da página da aula.
