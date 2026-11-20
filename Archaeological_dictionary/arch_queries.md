# Все SQL-запросы проекта 2025, Археологический словарь

**СУБД:** SQLite

Параметры `?` - это плейсхолдеры для параметризации.

---

## DDL: схема данных

```sql
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
```

---

## 1. DML: вставка данных (`INSERT`)

*Демонстрирует: placeholder-параметры, `INSERT` с неполными данными.*

**1.1. Термин: 4 поля**

```sql
INSERT INTO Term (word, latin, definition, extra_info) VALUES (?, ?, ?, ?);
```

**1.2. Ссылка: 3 поля**

```sql
INSERT INTO Link (word, latin, link) VALUES (?, ?, ?);
```

**1.3. Археолог: 6 полей**

```sql
INSERT INTO Archaeologist (surname, surname_lat, name, years, achievements, extra_info)
VALUES (?, ?, ?, ?, ?, ?);
```

---

## 2. DML: чтение и агрегация (`SELECT`)

**2.1. Полная выборка таблицы** (имя таблицы подставляется из контролируемого списка: `Term` / `Link` / `Archaeologist`).

*Демонстрирует: динамический `SELECT` по имени таблицы.*

```sql
SELECT * FROM {table_name};
```

**2.2. Агрегация «заполненности» полей.**

*Демонстрирует: `COUNT`, `DISTINCT`, `SUM`, `CASE`, динамическое выражение.*
*Зачем: среднее число заполненных полей на статью (для графиков).*

```sql
SELECT DISTINCT COUNT(*),
       SUM((CASE WHEN col1 IS NOT NULL AND col1 != '' THEN 1 ELSE 0 END) + ...)
FROM {table};
```

---

## 3. DML: изменение данных (`UPDATE`)

*Демонстрирует: `UPDATE`, `SET`, `WHERE`, точечное обновление по первичному ключу.*

**3.1. Обновление термина по `id`**

```sql
UPDATE Term
SET word = ?, latin = ?, definition = ?, extra_info = ?
WHERE id = ?;
```

**3.2. Обновление ссылки по `id`**

```sql
UPDATE Link
SET word = ?, latin = ?, link = ?
WHERE id = ?;
```

**3.3. Обновление археолога по `id`**

```sql
UPDATE Archaeologist
SET surname = ?, surname_lat = ?, name = ?, years = ?, achievements = ?, extra_info = ?
WHERE id = ?;
```

---

## 4. DML: удаление данных (`DELETE`)

*Демонстрирует: `DELETE`, удаление по первичному ключу (имя таблицы из контролируемого списка).*

```sql
DELETE FROM {table_name} WHERE id = ?;
```
