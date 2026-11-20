-- ============================================================
--  SQL-кейс: словарь археологических статей
--  СУБД: SQLite
--  Параметры-заглушки "?" — это placeholders для параметризации

-- ============================================================


-- ------------------------------------------------------------
-- 0. DDL: схема данных 
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Term (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  word text,
  latin text,
  definition text,
  extra_info text
);

CREATE TABLE IF NOT EXISTS Link (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  word text,
  latin text,
  link text
);

CREATE TABLE IF NOT EXISTS Archaeologist (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  surname text,
  surname_lat text,
  name text,
  years text,
  achievements text,
  extra_info text
);


-- ============================================================
-- 1. DML: ВСТАВКА ДАННЫХ (INSERT)
-- ============================================================

-- Демонстрирует: placeholder-параметры, INSERT с неполными данными.  
-- 1.1. Термин: 4 поля
INSERT INTO Term (word, latin, definition, extra_info) VALUES (?, ?, ?, ?);
-- 1.2. Ссылка: 3 поля
INSERT INTO Link (word, latin, link) VALUES (?, ?, ?);
-- 1.3. Археолог: 6 полей
INSERT INTO Archaeologist (surname, surname_lat, name, years, achievements, extra_info)
VALUES (?, ?, ?, ?, ?, ?);


-- ============================================================
-- 2. DML: ЧТЕНИЕ И АГРЕГАЦИЯ (SELECT)
-- ============================================================

-- 2.1 Полная выборка таблицы (имя таблицы подставляется из контролируемого списка: Term / Link / Archaeologist).
-- Демонстрирует: динамический SELECT по имени таблицы.
SELECT * FROM {table_name};

-- 2.2 Агрегация «заполненности» полей.
-- Демонстрирует: COUNT, DISTINCT, SUM, CASE, динамическое выражение.
-- Зачем: среднее число заполненных полей на статью (для графиков).
SELECT DISTINCT COUNT(*),
       SUM((CASE WHEN col1 IS NOT NULL AND col1 != '' THEN 1 ELSE 0 END) + ...)
FROM {table};


-- ============================================================
-- 3. DML: ИЗМЕНЕНИЕ ДАННЫХ (UPDATE)
-- ============================================================

-- Демонстрирует: UPDATE, SET, WHERE,точечное обновление по первичному ключу. 
-- 3.1 Обновление термина по id
UPDATE Term
SET word = ?, latin = ?, definition = ?, extra_info = ?
WHERE id = ?;

-- 3.2 Обновление ссылки по id
UPDATE Link
SET word = ?, latin = ?, link = ?
WHERE id = ?;

-- 3.3 Обновление археолога по id
UPDATE Archaeologist
SET surname = ?, surname_lat = ?, name = ?, years = ?, achievements = ?, extra_info = ?
WHERE id = ?;


-- ============================================================
-- 4. DML: УДАЛЕНИЕ ДАННЫХ (DELETE)
-- ============================================================

-- Демонстрирует: DELETE, удаление по первичному ключу (имя таблицы из контролируемого списка)
DELETE FROM {table_name} WHERE id = ?;
