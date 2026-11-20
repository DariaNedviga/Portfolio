-- ============================================================
--  SQL-кейс: словарь археологических статей
--  СУБД: SQLite
--  Запросы сгруппированы по навыкам (см. комментарии-секции).
--  Параметры-заглушки "?" — это placeholders для параметризации
--  (защита от SQL-инъекций), значения передаются из кода.
-- ============================================================


-- ------------------------------------------------------------
-- 0. DDL: схема данных (восстановлена из проекта)
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
--    Навыки: параметризация, работа с NULL, разные схемы.
-- ============================================================

-- 1.1 Термин: 4 поля; latin может быть NULL (нет латинского написания)
-- Демонстрирует: placeholder-параметры, INSERT с неполными данными.
INSERT INTO Term (word, latin, definition, extra_info) VALUES (?, ?, ?, ?);

-- 1.2 Ссылка: 3 поля; latin может быть NULL
-- Демонстрирует: INSERT в таблицу с иной схемой.
INSERT INTO Link (word, latin, link) VALUES (?, ?, ?);

-- 1.3 Археолог: 6 полей
-- Демонстрирует: INSERT в широкую таблицу, несколько текстовых полей.
INSERT INTO Archaeologist (surname, surname_lat, name, years, achievements, extra_info)
VALUES (?, ?, ?, ?, ?, ?);


-- ============================================================
-- 2. ЧТЕНИЕ И АГРЕГАЦИЯ (SELECT)
--    Навыки: COUNT, DISTINCT, SUM, CASE, динамические выражения.
-- ============================================================

-- 2.1 Полная выборка таблицы (имя таблицы подставляется из
--     контролируемого списка: Term / Link / Archaeologist).
-- Демонстрирует: динамический SELECT по имени таблицы.
-- ВАЖНО: {table_name} — не пользовательский ввод, иначе инъекция.
SELECT * FROM {table_name};

-- 2.2 Агрегация «заполненности» полей.
--     expr_sum собирается в коде как:
--     (CASE WHEN col IS NOT NULL AND col != '' THEN 1 ELSE 0 END) + ...
-- Демонстрирует: COUNT, DISTINCT, SUM, CASE, динамическое выражение.
-- Зачем: среднее число заполненных полей на статью (для графиков).
SELECT DISTINCT COUNT(*),
       SUM((CASE WHEN col1 IS NOT NULL AND col1 != '' THEN 1 ELSE 0 END) + ...)
FROM {table};

-- 2.3 Пример раскрытого варианта 2.2 для таблицы Term
--     (как это выглядит после подстановки колонок):
SELECT DISTINCT COUNT(*),
       SUM(
           (CASE WHEN word       IS NOT NULL AND word       != '' THEN 1 ELSE 0 END) +
           (CASE WHEN latin      IS NOT NULL AND latin      != '' THEN 1 ELSE 0 END) +
           (CASE WHEN definition IS NOT NULL AND definition != '' THEN 1 ELSE 0 END) +
           (CASE WHEN extra_info IS NOT NULL AND extra_info != '' THEN 1 ELSE 0 END)
       ) AS filled_fields
FROM Term;


-- ============================================================
-- 3. ИЗМЕНЕНИЕ ДАННЫХ (UPDATE)
--    Навыки: точечное обновление по первичному ключу.
-- ============================================================

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
-- 4. УДАЛЕНИЕ ДАННЫХ (DELETE)
--    Навыки: удаление по первичному ключу, параметризация.
-- ============================================================

-- 4.1 Удаление статьи по id (имя таблицы — из контролируемого списка)
DELETE FROM {table_name} WHERE id = ?;
