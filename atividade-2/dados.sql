-- Atividade 2 · dados de exemplo. NÃO edite este arquivo.
-- Ele só funciona depois que o seu schema.sql criar as três tabelas
-- com exatamente estes nomes de tabela e de coluna.

INSERT INTO events (id, title, date, capacity) VALUES
  (1, 'Oficina de Python',    '2026-10-10',  2),
  (2, 'Semana de Tecnologia', '2026-10-20', 40),
  (3, 'Hackathon Trilha',     '2026-11-07', 30),
  (4, 'Palestra de Carreira', '2026-09-28', 80);

INSERT INTO users (id, name, email) VALUES
  (1, 'Ana',   'ana@example.org'),
  (2, 'Bruno', 'bruno@example.org'),
  (3, 'Carla', 'carla@example.org'),
  (4, 'Diego', 'diego@example.org');

INSERT INTO registrations (id, event_id, user_id) VALUES
  (1, 1, 1),
  (2, 1, 2),
  (3, 2, 1),
  (4, 2, 3),
  (5, 3, 3),
  (6, 4, 4);
